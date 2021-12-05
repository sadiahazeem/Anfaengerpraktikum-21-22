import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

x, y = np.genfromtxt('dataB.txt', unpack=True)
x *=1e3
y /=7.5

def f(t, a):
    return 1/((np.sqrt(1+a**2*(t*2*np.pi)**2)))

parameters, pcov = curve_fit(f, x, y, p0=(0.1))
print(parameters, np.sqrt(np.diag(pcov)), sep='\n')

def g(t):
    return 1/(np.sqrt(1+(t*2*np.pi*0.0007531)**2))

t_plot = np.linspace(-0.1, 52, 1000)*1e3

plt.grid(True, linewidth=0.5)
plt.plot(x, y, 'x', label='Messdaten')
plt.plot(t_plot, f(t_plot, *parameters), 'r-', label='Fit')
plt.plot(t_plot, g(t_plot), 'g-', label='Originalfunktion')
plt.xscale('log')
plt.xlim(100, 52*1e3)
plt.xlabel(r'$f \mathbin{/} \unit{\hertz}$')
plt.ylabel(r'$\frac{U_c}{U_0}$')
plt.legend(loc='best')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot2.pdf')

