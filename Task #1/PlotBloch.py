from qutip import Bloch
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

figure = plt.figure(figsize=[6, 6])
ax = Axes3D(figure, azim=-120, elev=30)
sphere = Bloch(axes=ax)
sphere.zlabel = ['z', '-z']

# init the data of the MRI.
t = 1
M0 = 1                                      # mag of M0
T1 = 6                                     # T1 Value
T2 = 3                                      # T2 Value

Mxy = M0 * np.exp(-t/T2)
# Mx = M0 * np.exp(-t/T2) * np.sin(2*np.pi*1*t)
# My = M0 * np.exp(-t/T2) * np.cos(2*np.pi*1*t)
Mz = M0 * (1 - np.exp(-t/T1))
M = [Mxy, Mxy, 0]
# M = [Mx, My, 0]
sphere.add_vectors(M)

def updateAnimation(t):
    global Mxy, Mz, Mx, My
    sphere.clear()
    Mxy = M0 * np.exp(-t / T2)
    # Mx = M0 * np.exp(-t / T2) * np.sin(2 * np.pi * 1 * t)
    # My = M0 * np.exp(-t / T2) * np.cos(2 * np.pi * 1 * t)
    Mz = M0 * (1 - np.exp(-t / T1))
    M[0] = Mxy
    M[1] = Mxy
    # M[0] = Mx
    # M[1] = My
    M[2] = Mz
    sphere.add_vectors(M)
    sphere.make_sphere()

ani = FuncAnimation(figure, updateAnimation, frames=np.arange(1, 200, 0.1), interval=50)
# ani.save("RelaxationWithPrecession.mp4")
plt.show()
