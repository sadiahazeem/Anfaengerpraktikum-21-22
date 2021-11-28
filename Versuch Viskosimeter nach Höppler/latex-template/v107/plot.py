import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from uncertainties.unumpy import (
    nominal_values as noms,
    std_devs as stds,
)
def linregress(x, y):
    assert len(x) == len(y)

    x, y = np.array(x), np.array(y)

    N = len(y)
    Delta = N * np.sum(x**2) - (np.sum(x))**2

    A = (N * np.sum(x * y) - np.sum(x) * np.sum(y)) / Delta
    B = (np.sum(x**2) * np.sum(y) - np.sum(x) * np.sum(x * y)) / Delta

    sigma_y = np.sqrt(np.sum((y - A * x - B)**2) / (N - 2))

    A_error = sigma_y * np.sqrt(N / Delta)
    B_error = sigma_y * np.sqrt(np.sum(x**2) / Delta)
    return A, A_error, B, B_error

def f(x,a,b):
    return a*x + b

T_plot = np.linspace(0.003, 0.0034, 1000)

T = np.array([298.15,302.15,305.15,307.15,309.15,311.15,313.15,315.15,317.15,319.15,321.15,323.15])
etaH = np.array([1.1386,1.0554,0.9657,0.9528,0.9273,0.8821,0.8398,0.8255,0.7907,0.7701,0.7427,0.7201]) * 1e-3
etaHerr = np.array([0.0473,0.0440,0.0404,0.0404,0.0391,0.0379,0.0351,0.0343,0.0340,0.0323,0.0316,0.0361]) * 1e-3
EtaH = unp.uarray(etaH, etaHerr)
etaZ = np.array([1.1705,1.1107,0.9922,0.9740,0.9595,0.9199,0.8772,0.8440,0.8073,0.7923,0.7606,0.7396]) * 1e-3
etaZerr = np.array([0.0412,0.0391,0.0354,0.0346,0.0344,0.0330,0.0318,0.0314,0.0285,0.0284,0.0269,0.0263]) * 1e-3
EtaZ = unp.uarray(etaZ,etaZerr)

print(linregress(1/T, np.log(etaH)))
print(linregress(1/T, np.log(etaZ)))

a1, aerr1, b1, berr1 = linregress(1/T, np.log(etaH))
a2, aerr2, b2, berr2 = linregress(1/T, np.log(etaZ))

plt.grid(True)
plt.errorbar(1/T,np.log(noms(EtaH)), yerr = np.log(stds(EtaH) + noms(EtaH)) - np.log(noms(EtaH)), fmt='r_', label = 'Daten hin')
plt.plot(T_plot, f(T_plot, a1,b1), 'r-', label='lineare Regression hin')
plt.errorbar(1/T,np.log(noms(EtaZ)), yerr = np.log(stds(EtaZ) + noms(EtaZ)) - np.log(noms(EtaZ)), fmt='b_', label = 'Daten zurück')
plt.plot(T_plot, f(T_plot, a2,b2), 'b-', label='lineare Regression zurück')
plt.xlim(0.003)
plt.xlabel(r'$T^{-1} \mathbin{/} \unit{\kelvin}^{-1}$')
plt.ylabel(r'$\ln\left(\frac{\eta}{\unit{\pascal\second}}\right)$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')
