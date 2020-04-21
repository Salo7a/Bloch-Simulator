from qutip import Bloch
import numpy as np
import matplotlib
from scipy.spatial.transform import Rotation as R
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

matplotlib.use("TkAgg")

figure = plt.figure(figsize=[6, 6])
ax = Axes3D(figure, azim=-120, elev=30)
sphere = Bloch(axes=ax)
sphere.zlabel = ['z', '-z']

# init the data of the MRI.
t = 0
M0 = 1  # mag of M0
T1 = 6  # T1 Value
T2 = 3  # T2 Value

Mxy = M0
# Mx = M0 * np.exp(-t/T2) * np.sin(2*np.pi*1*t)
# My = M0 * np.exp(-t/T2) * np.cos(2*np.pi*1*t)
Mz = M0 * (1 - np.exp(-t / T1))
# M = [Mxy, Mxy, 0]
# M = [Mx, My, 0]
M = [0, 0, 1]
sphere.add_vectors(M)
rotated = False
i = 0
elapsed = 0

def yrot(vector, theta):
    vec = vector

    rotation_degrees = theta
    rotation_radians = np.radians(rotation_degrees)
    rotation_axis = np.array([0, 1, 0])

    rotation_vector = rotation_radians * rotation_axis
    rotation = R.from_rotvec(rotation_vector)

    sec = rotation.apply(vec)
    rotation_degrees = theta / 2
    rotation_radians = np.radians(rotation_degrees)
    rotation_axis = np.array([0, 0, 1])

    rotation_vector = rotation_radians * rotation_axis
    rotation = R.from_rotvec(rotation_vector)
    return rotation.apply(sec)


def updateAnimation(t):
    global Mxy, Mz, Mx, My, M, i, rotated, elapsed
    sphere.clear()
    if i < 90:
        i += 1
        r = yrot(M, 1)
        M = r
    else:
        if not rotated:
            # r = yrot(M, 1)
            # M = r
            rotated = True
            elapsed = t
        Mxy = M0 * np.exp(-(t - elapsed + 1) / T2)
        # Mx = M0 * np.exp(-t / T2) * np.sin(2 * np.pi * 1 * t)
        # My = M0 * np.exp(-t / T2) * np.cos(2 * np.pi * 1 * t)
        Mz = M0 * (1 - np.exp(-(t - elapsed) / T1))
        M[0] = Mxy
        M[1] = Mxy
        # M[0] = Mx
        # M[1] = My
        M[2] = Mz
        print(M)
    sphere.add_vectors(M)
    sphere.make_sphere()


ani = FuncAnimation(figure, updateAnimation, frames=np.arange(1, 40, 0.1), interval=30)
# ani.save("RelaxationWithPrecession.mp4")
plt.show()

r = yrot(M, 90)
M = r
i += 1
print(M)
