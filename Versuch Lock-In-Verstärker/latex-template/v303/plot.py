import matplotlib.pyplot as plt
import numpy as np

r, U = np.genfromtxt('data_led.txt', unpack=True)
r *= 1e-2
def f(x):
    return 1/x**2

plt.figure()
plt.plot(r, U, label='Messdaten')
plt.plot(r, f(r), label=r'$1/r^2$')
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
