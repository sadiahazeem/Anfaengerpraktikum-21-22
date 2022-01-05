import matplotlib.pyplot as plt
import numpy as np
# außerdem (evtl löschen wenn nciht benötigt)
from scipy import integrate
import uncertainties.unumpy as unp 
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy.optimize import curve_fit
from uncertainties import ufloat


# die werte allgemein:

R1=67.2 #ohm
R2=682 #ohm
L=16.87*10**(-3) #H
C=2.06*10**(-9) #F


# noch mal werte mit fehlern hier ergänzen?









x = np.linspace(0, 10, 1000)
y = x ** np.sin(x)

plt.subplot(1, 2, 1)
plt.plot(x, y, label='Kurve')
plt.xlabel(r'$\alpha \mathbin{/} \unit{\ohm}$')
plt.ylabel(r'$y \mathbin{/} \unit{\micro\joule}$')
plt.legend(loc='best')

plt.subplot(1, 2, 2)
plt.plot(x, y, label='Kurve')
plt.xlabel(r'$\alpha \mathbin{/} \unit{\ohm}$')
plt.ylabel(r'$y \mathbin{/} \unit{\micro\joule}$')
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')





# teilaufgabe d (phi diagramm)

w,a,b=np.genfromtxt("data1.txt", delimiter=", ", unpack=True, skip_header=1)
phi=a/b*np.pi
print("w    &   a   &   b   &   phi")  # hinter phi \n weggemacht
for x in range(0,len(w)-1):
    print(f"{w[x]} & {a[x]} & {b[x]} & {phi[x].round(2)} \\\\")

plt.plot(w,phi,"rx",label="Phasenverschiebung")
plt.xlabel("$w\;/\;kHz$")
plt.ylabel("$\phi \;/\;$rad")
plt.legend(loc="best")
plt.savefig("build/plotd.pdf",bbox_inches='tight')
plt.show()