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

#
#
#
#x = np.linspace(0, 10, 1000)
#y = x ** np.sin(x)
#
#plt.subplot(1, 2, 1)
#plt.plot(x, y, label='Kurve')
#plt.xlabel(r'$\alpha \mathbin{/} \unit{\ohm}$')
#plt.ylabel(r'$y \mathbin{/} \unit{\micro\joule}$')
#plt.legend(loc='best')
#
#plt.subplot(1, 2, 2)
#plt.plot(x, y, label='Kurve')
#plt.xlabel(r'$\alpha \mathbin{/} \unit{\ohm}$')
#plt.ylabel(r'$y \mathbin{/} \unit{\micro\joule}$')
#plt.legend(loc='best')
#
## in matplotlibrc leider (noch) nicht möglich
#plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
#plt.savefig('build/plot.pdf')
#


# teilaufgabe c (diagramm u gegen f, mit theoriekurve? -- halblog: y ist ln(U/U0) )

line_w=np.linspace(20,60)
line_W=line_w*1000
U_0=4

def U_funktion(w):
    return 1.5/(np.sqrt((1-L*C*w**2)**2+(w*R2*C)**2))  

def lnU_funktion(U):
    return np.log(U/4)

line_w=np.linspace(20,60)
line_W=line_w*1000

w,U=np.genfromtxt("data2.txt", delimiter=", ", unpack=True, skip_header=1)

lnU = lnU_funktion(U)
U_fkt = U_funktion(line_W*6.6)
lnU_theorie = np.log(U_fkt) # war jz unnötig, man hätte den ln direkt oben in der ursprünglichen funktion einfügen können...

plt.plot(line_w, lnU_theorie,label="Theoriekurve")
plt.plot(w,lnU,"r+",label="Messwerte")
plt.ylabel("$ln(U_C/U_0)\;/\;V$")
plt.xlabel("$f\,/\,kHz$")
plt.legend()
plt.savefig("build/plotc.pdf",bbox_inches='tight')
plt.close()



# teilaufgabe c (diagramm u gegen f, linear)

plt.plot(line_w,U_funktion(line_W*6.6),label="Theoriekurve")
plt.plot(w,U,"r+",label="Messwerte")
plt.ylabel("$U\;/\;V$")
plt.xlabel("$f\,/\,kHz$")
plt.legend()
plt.savefig("build/plotc2.pdf",bbox_inches='tight')
plt.close()









# teilaufgabe d (phi diagramm, halblog: y logarithmisch, )

w,a,b=np.genfromtxt("data1.txt", delimiter=", ", unpack=True, skip_header=1)
phi=a/b*np.pi
print("w    &   a   &   b   &   phi")  # hinter phi \n weggemacht
for x in range(0,len(w)-1):
    print(f"{w[x]} & {a[x]} & {b[x]} & {phi[x].round(2)} \\\\")

plt.plot(w,np.log(phi),"rx",label="Phasenverschiebung")
plt.xlabel("$f\;/\;kHz$")
plt.ylabel("$ln(\phi) \;/\;$rad")
plt.legend(loc="best")
plt.savefig("build/plotd.pdf",bbox_inches='tight')
plt.close()



# teilaufgabe d (phi diagramm, linear um pi/2, und resonanzfrequenz??)

print("w    &   a   &   b   &   phi\n")
for x in range(0,len(w)-1):
    print(f"{w[x]} & {a[x]} & {b[x]} & {phi[x].round(2)} \\\\")

plt.plot(w,phi,"rx",label="Phasenverschiebung")
plt.xlabel("$f\;/\;kHz$")
plt.ylabel("$\Delta \phi \;/\;$rad")
plt.legend(loc="best")
plt.savefig("build/plotd2.pdf",bbox_inches='tight')
plt.close()