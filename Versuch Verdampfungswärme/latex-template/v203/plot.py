import matplotlib.pyplot as plt
import numpy as np

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

T, P = np.genfromtxt('Dampfdruck30-1000.txt', unpack=True)
P *= 1e-3
T += 273.15
P /= 1.024

T_plot = np.linspace(1/375,1/290,500)
print(linregress(1/T, np.log(P)))

a1, aerr1, b1, berr1 = linregress(1/T, np.log(P))

plt.grid(True)
plt.plot(1/T, np.log(P), 'x', label='Messdaten')
plt.plot(T_plot, f(T_plot, a1, b1), 'r-', label='Ausgleichsrechnung')#(-4725.561124057688, 36.93508957789806, 12.647246969003449, 0.11133452081004634)
plt.xlabel(r'$T^{-1}/K$')
plt.ylabel(r'$\ln(p)$')
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')
