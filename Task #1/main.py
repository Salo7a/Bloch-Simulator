# Importing Packages
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox
import numpy as np
import blochGUI as m
from imageModel import ImageModel

#importing module
import logging

#Create and configure logger
logging.basicConfig(level=logging.DEBUG,
                    filename="playground.log",
					format='%(lineno)s - %(levelname)s - %(message)s',
					filemode='w')

#Creating an object
logger=logging.getLogger()

class blochSimulator(m.Ui_MainWindow):

    def __init__(self, starterWindow):
        """
        Main loop of the UI
        :param mainWindow: QMainWindow Object
        """
        super(blochSimulator, self).setupUi(starterWindow)

        # Images List
        self.imageWidgets = [self.img1_original,  self.img1_updated]

        # Widgets List
        self.widgets = [self.nonUniWidget, self.blochWidget]

        # Setup Load and Combo Connections
        self.load_btn.clicked.connect(self.loadFile)
        self.combo_input1.activated.connect(self.updateCombosChanged)

        self.setupImagesView()
        self.widgetConfiguration()

        logger.info("The Application started successfully")

    def loadFile(self):
        """
        Load the File from User
        :param imgID: 0 or 1
        :return:
        """
        # Open File & Check if it was loaded correctly
        logger.info("Browsing the files...")
        self.filename, self.format = QtWidgets.QFileDialog.getOpenFileName(None, "Load Image", '/home', "*.jpg;;" "*.jpeg;;" "*.png;;" "*.svg;;")
        imgName = self.filename.split('/')[-1]
        if self.filename == "":
            pass
        else:
            self.imageModel= ImageModel(self.filename)
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
        widget.view.setRange(xRange=[0, self.imageModel.imgShape[0]], yRange=[0, self.imageModel.imgShape[1]], padding=0)
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


    def showMessage(self, header, message, button, icon):
        msg = QMessageBox()
        msg.setWindowTitle(header)
        msg.setText(message)
        msg.setIcon(icon)
        msg.setStandardButtons(button)
        x = msg.exec_()


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
