import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

r, U = np.genfromtxt('data_led.txt', unpack=True)
r *= 1e-2

def g(x,a,b):
    return a/x + b

def f(x,a,b):
    return a/x**2 + b
def co1(x,a,b,c):
    return a*np.cos(b*x+c)

def co2(x,a,b,c,d):
    return a*np.cos(b*x+c) + d

parameters, pcov = curve_fit(f, r, U, p0=(1,1))
print(parameters, np.sqrt(np.diag(pcov)), sep='\n')

parameters2, pcov2 = curve_fit(g, r, U, p0=(1,1))
print(parameters2, np.sqrt(np.diag(pcov2)), sep='\n')

r_plot=np.linspace(0.05,0.7,500)

plt.figure()
plt.plot(r, U, 'x', label='Messdaten')
plt.plot(r_plot, g(r_plot, *parameters2), label=r'$\varpropto 1/r$')
plt.plot(r_plot, f(r_plot, *parameters), label=r'$\varpropto 1/r^2$')
plt.legend(loc='best')
plt.xlabel(r'$r \mathbin{/} \unit{\meter}$')
plt.ylabel(r'$U \mathbin{/} \unit{\volt}$')
# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/Led-Messung.pdf')

phi, U = np.genfromtxt('data_verrauscht.txt', unpack=True)
phi *=2*np.pi/360

parameters3, pcov3 = curve_fit(co2, phi, U, p0=(10,1,1,10))
print(parameters3, np.sqrt(np.diag(pcov3)), sep='\n')

phiplot = np.linspace(0,2*np.pi,500)

plt.figure()
plt.plot(phi, U, 'x', label='Messdaten')
plt.plot(phiplot, co2(phiplot, *parameters3), label = 'Fit')
plt.legend(loc='best')
plt.xlabel(r'$\varphi \mathbin{/} rad$')
plt.ylabel(r'$U \mathbin{/} \unit{\milli\volt}$')
# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/verrauscht.pdf')

phi, U = np.genfromtxt('data_unverrauscht.txt', unpack=True)
phi *=2*np.pi/360

parameters4, pcov4 = curve_fit(co2, phi, U, p0=(10,1,1,10))
print(parameters4, np.sqrt(np.diag(pcov4)), sep='\n')

phiplot = np.linspace(0,2*np.pi,500)

plt.figure()
plt.plot(phi, U, 'x', label='Messdaten')
plt.plot(phiplot, co2(phiplot, *parameters4), label = 'Fit')
plt.legend(loc='best')
plt.xlabel(r'$\varphi \mathbin{/} rad$')
plt.ylabel(r'$U \mathbin{/} \unit{\volt}$')
# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/unverrauscht.pdf')