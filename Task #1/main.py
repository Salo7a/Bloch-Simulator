# Importing Packages
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox
import numpy as np
from pyqtgraph import mkPen
from smurves import surgebinder

import blochGUI as m
from imageModel import ImageModel

# importing module
import logging

# Create and configure logger
logging.basicConfig(level=logging.DEBUG,
                    filename="playground.log",
                    format='%(lineno)s - %(levelname)s - %(message)s',
                    filemode='w')

# Creating an object
logger = logging.getLogger()


class blochSimulator(m.Ui_MainWindow):

    def __init__(self, starterWindow):
        """
        Main loop of the UI
        :param mainWindow: QMainWindow Object
        """
        super(blochSimulator, self).setupUi(starterWindow)

        # Images List
        self.imageWidgets = [self.img1_original, self.img1_updated]

        # Widgets List
        self.widgets = [self.nonUniWidget, self.blochWidget]

        # Setup Load and Combo Connections
        self.load_btn.clicked.connect(self.loadFile)
        self.combo_input1.activated.connect(self.updateCombosChanged)

        self.setupImagesView()
        self.widgetConfiguration()

        # init the data of the MRI.
        self.dt = 1  # 1 ms delta-time.
        self.T = 1000  # 1000 ms time.
        self.N = int(self.T / self.dt) + 1  # number of time steps.
        # self.df = 2                            # freq of oscillation
        self.tr = 300  # time of repetion the Rf pulse
        self.te = 100  # time to measure the signal
        self.M0 = 1  # mag of M0
        self.time = np.linspace(0, self.T, self.N)  # list of the time to plot in x-axis

        # connect the pushbutton
        self.pushButton.clicked.connect(self.Mxyz)

        # change the lables of the sliders
        self.sliders = [self.fSlider, self.t1Slider, self.t2Slider]  # list of all the sliders
        self.slidersLable = [self.fLabel, self.t1Label, self.t2Label]  # list of all the labels of sliders
        for i in range(len(self.sliders)):  # set the albel to 0 value
            self.slidersLable[i].setText(str(self.sliders[i].value()))

        # conncet the sliders to the function
        self.fSlider.valueChanged.connect(lambda: self.changeLable(0))
        self.t1Slider.valueChanged.connect(lambda: self.changeLable(1))
        self.t2Slider.valueChanged.connect(lambda: self.changeLable(2))

        # Connect Generate Button To Function
        self.generatebutton.clicked.connect(self.PlotBz)
        self.nonUniWidget.plotItem.setLabel(axis='left', text="Tesla")
        self.nonUniWidget.plotItem.setLabel(axis='bottom', text="Point")

        logger.info("The Application started successfully")

    def loadFile(self):
        """
        Load the File from User
        :param imgID: 0 or 1
        :return:
        """
        # Open File & Check if it was loaded correctly
        logger.info("Browsing the files...")
        self.filename, self.format = QtWidgets.QFileDialog.getOpenFileName(None, "Load Image", '/home',
                                                                           "*.jpg;;" "*.jpeg;;" "*.png;;" "*.svg;;")
        imgName = self.filename.split('/')[-1]
        if self.filename == "":
            pass
        else:
            self.imageModel = ImageModel(self.filename)
            self.displayImage(self.imageModel.imgByte, self.img1_original)
            self.combo_input1.setEnabled(True)
            logger.info(f"Added Image: {imgName} successfully")

    def setupImagesView(self):
        """
        Adjust the shape and scales of the widgets
        Remove unnecessary options
        :return:
        """
        for widget in self.imageWidgets:
            widget.ui.histogram.hide()
            widget.ui.roiBtn.hide()
            widget.ui.menuBtn.hide()
            widget.ui.roiPlot.hide()
            widget.getView().setAspectLocked(False)
            widget.view.setAspectLocked(False)

    def widgetConfiguration(self):
        """
        Sets the plotting configurations
        :return:
        """
        # Channel 1
        # Setting ranges of the x and y axis
        for widget in self.widgets:
            widget.setXRange(min=0, max=1000)
            widget.setMinimumSize(QtCore.QSize(500, 200))
            widget.plotItem.showGrid(True, True, alpha=0.8)
            widget.plotItem.setLabel("bottom", text="Time (ms)")

    def displayImage(self, data, widget):
        """
        Display the given data
        :param data: 2d numpy array
        :param widget: ImageView object
        :return:
        """
        widget.setImage(data)
        widget.view.setRange(xRange=[0, self.imageModel.imgShape[0]], yRange=[0, self.imageModel.imgShape[1]],
                             padding=0)
        widget.ui.roiPlot.hide()

    def updateCombosChanged(self):
        selectedComponent = self.combo_input1.currentText().lower()

        fShift = np.fft.fftshift(self.imageModel.dft)
        magnitude = 20 * np.log(np.abs(fShift))
        phase = np.angle(fShift)
        real = 20 * np.log(np.real(fShift))
        imaginary = np.imag(fShift)

        if selectedComponent == "magnitude":
            self.displayImage(magnitude, self.img1_updated)
        elif selectedComponent == "phase":
            self.displayImage(phase, self.img1_updated)
        elif selectedComponent == "real":
            self.displayImage(real, self.img1_updated)
        elif selectedComponent == "imaginary":
            self.displayImage(imaginary, self.img1_updated)

        logger.info(f"Viewing {selectedComponent} Component Of The Image")

    def changeLable(self, sliderIndex):
        '''
        change the label w.r.t to the slider 
        '''
        self.slidersLable[sliderIndex].setText(str(self.sliders[sliderIndex].value()))

    def Mxyz(self):
        '''
        call the value of Mxy and Mz 
        '''
        self.blochWidget.plotItem.clear()  # clear the widget fron any previous plot

        df = self.fSlider.value()  # get the value of f
        T1 = self.t1Slider.value()  # get the value of T1
        T2 = self.t2Slider.value()  # get the value of T2

        x = np.linspace(0, self.te, len(self.time))  # list of the time taking to take a photo
        Mxy = self.M0 * (np.exp(-x / T2)) * np.cos(2 * np.pi * df * (x / T2))  # Mxy oscillation
        line = self.M0 * np.exp(-x / T2)  # the decay of Mxy

        tr = np.linspace(0, self.tr, len(self.time))  # list of the time taking to Tr
        Mz = self.M0 * (1 - np.exp(-tr / T1))  # increasing of Mz
        plot = [Mxy, Mz, line]  # list of all plotting data

        colors = ['b', 'r', 'w']

        # plot the data 
        for i in range(len(plot)):
            self.blochWidget.plotItem.plot(self.time, plot[i],
                                           pen=mkPen(colors.pop(), width=2, style=QtCore.Qt.SolidLine))

    def showMessage(self, header, message, button, icon):
        msg = QMessageBox()
        msg.setWindowTitle(header)
        msg.setText(message)
        msg.setIcon(icon)
        msg.setStandardButtons(button)
        x = msg.exec_()

    def GenerateNonUniform(self, Tesla=1.5, MaxDeviation=5, Length=2000):
        start = Tesla - Tesla * (MaxDeviation / 100)
        end = Tesla + Tesla * (MaxDeviation / 100)
        curve = surgebinder(n_curves=1,
                            x_interval=[0.0, float(Length)],
                            y_interval=[start, end],
                            n_measure=Length,
                            direction_maximum=4)
        return np.asarray(curve)

    def PlotBz(self):
        Field = self.GenerateNonUniform()
        self.nonUniWidget.plotItem.clear()
        self.nonUniWidget.setXRange(0, 2000)
        self.nonUniWidget.plotItem.plot(Field[0, :, 0], Field[0, :, 1],
                                        pen=mkPen('c', width=2, style=QtCore.Qt.SolidLine))


def main():
    """
    the application startup functions
    :return:
    """
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = blochSimulator(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
