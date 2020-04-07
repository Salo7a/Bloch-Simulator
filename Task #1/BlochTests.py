import blochsimu
import numpy as np
from numpy import cos, sin, exp, pi
from scipy.spatial.transform import Rotation as R
M = np.array([1., 0, 0])
B = np.array([0.0, 0.0, 50e-6])
N = 10 ** 5

sim = blochsimu.Simulator(M, n_steps=100)

for i in range(sim._n_steps):
    print(sim.simulate_step(B, 2e-5))
# Variables
Mx, Mxo, My, Myo, Mz, Mzo = 0, 0, 0, 0, 0, 0
Mo = [0, 0, 1]
M = [Mx, My, Mz]
B = [0, 0, 0]
t = 0
T1 = 0
T2 = 0
Rx = Rz = Ry = None


# Transverse Relaxation

# Mx = Mxo * np.exp(-t / T2)
# My = np.exp(Myo, -t / T2)

# Longitudinal Relaxation
# Mz = 1 + [Mzo - 1] * exp(-t / T1)


def zrot(phi):
    return [[cos(phi), - sin(phi), 0], [sin(phi), cos(phi), 0], [0, 0, 1]]


def xrot(phi):
    return [[1, 0, 0], [0, cos(phi), -sin(phi)], [0, sin(phi), cos(phi)]]


def yrot(phi):
    return [[cos(phi), 0, sin(phi)], [0, 1, 0], [-sin(phi), 0, cos(phi)]]


def freeprecess(T, T1, T2, df):
    """Function simulates free precession and decay
    over a time interval T, given relaxation times T1 and T2
    and off-resonance df.  Times in ms, off-resonance in Hz."""

    phi = 2 * pi * df * T / 1000  # Resonant precession, radians.
    E1 = exp(-T / T1)
    E2 = exp(-T / T2)

    Afp = np.matrix([[E2, 0, 0], [0, E2, 0], [0, 0, E1]]) * zrot(phi)
    Bfp = [0, 0, 1 - E1]


vec = [0, 0, 1]

rotation_degrees = 90
rotation_radians = np.radians(rotation_degrees)
rotation_axis = np.array([0, 1, 0])

rotation_vector = rotation_radians * rotation_axis
rotation = R.from_rotvec(rotation_vector)
rotated_vec = rotation.apply(vec)

print(rotated_vec)
