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

U, t = np.genfromtxt('dataA.txt', unpack=True)

def f(x,a,b):
    return a*x + b

t_plot = np.linspace(-0.05, 1.4 + 0.05, 1000) * 1e-3
print(linregress(t * 1e-3, U))

a1, aerr1, b1, berr1 = linregress(t * 1e-3, U)
plt.grid(True, linewidth=0.5)
plt.plot(t * 1e-3 , U, 'x', label='Messdaten')
plt.plot(t_plot, f(t_plot, a1,b1), 'r-', label='lineare Regression')
#plt.xscale('log')
#plt.xlim(10e-5,10e-2)
plt.xlabel(r'$t \mathbin{/} \unit{\second}$')
plt.ylabel(r'$\ln\left(\frac{U_c}{U_0}\right)$')
plt.legend(loc='best')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')

