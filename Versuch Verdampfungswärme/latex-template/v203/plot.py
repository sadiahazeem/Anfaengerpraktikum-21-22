import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
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
#print(linregress(1/T, np.log(P)))

a1, aerr1, b1, berr1 = linregress(1/T, np.log(P))

plt.figure()
plt.grid(True)
plt.plot(1/T, np.log(P), 'x', label='Messdaten')
plt.plot(T_plot, f(T_plot, a1, b1), 'r-', label='Ausgleichsrechnung')#(-4725.561124057688, 36.93508957789806, 12.647246969003449, 0.11133452081004634)
plt.xlabel(r'$T^{-1}/\frac{1}{K}$')
plt.ylabel(r'$\ln(p)$')
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')

P, T = np.genfromtxt('Dampfdruck1-15.txt', unpack=True)
T +=273.15
P *=100000

def g(x,a,b,c,d):
    return a*x**3+b*x**2+c*x+d

parameters, pcov = curve_fit(g, T, P, p0=(1,1,1,1))
print(parameters, np.sqrt(np.diag(pcov)), sep='\n')

T_plot2 = np.linspace(375,470,500)

plt.figure()
plt.grid(True)
plt.plot(T, P, 'x', label='Messdaten')
plt.plot(T_plot2, g(T_plot2, *parameters), 'r-', label='Fit')
plt.xlabel(r'$T/K$')
plt.ylabel(r'$p/Pa$')
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot2.pdf')

def L1(x,p):
    return x*((8.314*x)/(2*p) + np.sqrt(np.square((8.314*x)/(2*p)) - 0.9/p))*(3*9.5245*0.1*x**2 - 2*1.0592*1000*x + 3.9451*100000)

plt.figure()
plt.grid(True)
plt.plot(T, L1(T,P), 'x', label='Messdaten')
plt.xlabel(r'$T/K$')
plt.ylabel(r'$L(T)/\unit{\joule\per\mol}$')
plt.legend(loc='best')

print(L1(T,P))

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot3.pdf')

def L2(x,p):
    return x*(8.314*x/(2*p) - np.sqrt((8.314*x/(2*p))**2 - 0.9/p))*(3*9.5245*0.1*x**2 - 2*1.0592*1000*x + 3.9451*100000)

plt.figure()
plt.grid(True)
plt.plot(T, L2(T,P), 'r-', label='Kurve der Messdaten')
plt.xlabel(r'$T/K$')
plt.ylabel(r'$L(T)/\unit{\joule\per\mol}$')
plt.legend(loc='best')

print(L2(T,P))

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot4.pdf')
