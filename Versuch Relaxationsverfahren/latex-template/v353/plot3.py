import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

x, y = np.genfromtxt('dataC.txt', unpack=True)
x *=1e3

def f(t, a, b):
    return a*np.arctan(b*t)

def g(t):
    return np.arctan(t*0.0069641)

parameters, pcov = curve_fit(f, x, y, p0=(1,0.1))
print(parameters)

t_plot = np.linspace(-0.1, 52, 1000)*1e3

plt.grid(True, linewidth=0.5)
plt.plot(x, y, 'x', label='Messdaten')
plt.plot(t_plot, f(t_plot, *parameters), 'r-', label='Fit')
plt.plot(t_plot, g(t_plot), 'g-', label='Originalfunktion')
plt.xscale('log')
plt.xlim(100, 52*1e3)
plt.ylim(0, 3)
plt.xlabel(r'$f \mathbin{/} \unit{\hertz}$')
plt.ylabel(r'$\phi \mathbin{/} \unit{\radian}$')
plt.legend(loc='best')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot3.pdf')