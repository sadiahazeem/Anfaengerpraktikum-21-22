import matplotlib.pyplot as plt
import numpy as np

y, x = np.genfromtxt('dataD.txt', unpack=True)
y /=3.6

phi = np.arange(0, np.pi/2, 0.01)

def f(x):
    return np.cos(x)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(x, y, 'x')
ax.plot(phi, f(phi))
ax.set_rmax(1.05)
ax.set_rlabel_position(270)
ax.grid(True)

plt.savefig('build/plot4.pdf')
