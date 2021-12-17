import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

r, U = np.genfromtxt('data_led.txt', unpack=True)
r *= 1e-2

def g(x,a,b):
    return a/x + b

def f(x,a,b):
    return a/x**2 + b

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



#plt.figure()
#plt.plot(r, U, label='Messdaten')
#plt.plot(r, f(r), label=r'$1/r^2$')
#plt.legend(loc='best')
#plt.xlabel(r'$r \mathbin{/} \unit{\meter}$')
#plt.ylabel(r'$U \mathbin{/} \unit{\volt}$')
## in matplotlibrc leider (noch) nicht möglich
#plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
#plt.savefig('build/Led-Messung.pdf')
