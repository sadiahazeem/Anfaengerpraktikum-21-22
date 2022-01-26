import matplotlib.pyplot as plt
import numpy as np
# außerdem (evtl löschen wenn doch nicht benötigt)
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


# die werte mit fehler:

R1_e=ufloat(67.2,0.01)#Ohm          
R2_e=ufloat(682,0.5)#Ohm
L_e=ufloat(16.87,0.05)*10**(-3)#H
C_e=ufloat(2.06,0.3)*10**(-9)#F



# 5a, plot zur abklingdauer, aus data3.txt

def funktiona(t,k):
    return 4*np.exp(-k*t)
def funktiona_theo(t,k):
    return 4*np.exp(-k*t)


t, UC=np.genfromtxt("data3.txt", delimiter=", ", unpack=True, skip_header=1)
UC=UC*2 #Volt - Umrechnung da Oszilator auf 2V/Div.
t=t*20*10**(-6) #s - Umrechnung da Oszillator auf 20us/Div.

#Messwerte plotten
tp=t*10**6
plt.plot(tp,UC,"rx",label="Messdaten")

#Messwerte fitten
line=np.linspace(0,tp[len(tp)-1])
params, cov= curve_fit(funktiona,tp,UC)
errors = np.sqrt(np.diag(cov))
unparams = unp.uarray(params,errors)
plt.plot(line,funktiona(line,*params),"g",label='Ausgleichs e-Funktion')

werte_params=f"""
    Berechnete Werte aus Messwert-Fit für Bausteine\\
    k=R/2L: {unparams[0]}\
    Tex=1/k {1/unparams[0]}\
    Reff: {unparams[0]*2*L}\
    L: {L_e}\\
    Theorie\
    k=R/2L: {R1_e/(2*L_e)}\n
    Rap: {np.sqrt(4*L/C)}                                       
     """                                                                    #Rap mit fehlern
print(werte_params)

#Theoriekurve plotten
#plt.plot(tp,funktiona_theo(t,R2/(2*L)),"b--",label="Theoriekurve")
plt.legend()
plt.xlabel("$t\;/\;\mu s$")
plt.ylabel("$U_C\;/\;V$")
plt.savefig("build/plot_Tex.pdf",bbox_inches='tight')
plt.close()










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
plt.axvline(x=23)    
plt.axvline(x=29.5)                                 # korrektur
plt.ylabel("$ln(U_C/U_0)\;/\;V$")                                
plt.xlabel("$f\,/\,kHz$")
plt.legend()
plt.savefig("build/plotc.pdf",bbox_inches='tight')
plt.close()



# teilaufgabe c (diagramm u gegen f, linear)

halbwert_Uc = [1.65/np.sqrt(2)]*len(w)

plt.plot(line_w,U_funktion(line_W*6.6),label="Theoriekurve")
plt.plot(w,U,"r+",label="Messwerte")
plt.plot(w,halbwert_Uc,"y",label="Halbwert") 
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
plt.ylabel("$\phi \;/\;$rad")
plt.legend(loc="best")
plt.savefig("build/plotd2.pdf",bbox_inches='tight')
plt.close()

line_w= np.linspace(5,60)
line_W=line_w*1000
plt.plot(line_w,np.sqrt(R2**2+(line_W*L-1/(line_W*C))**2),"r-",label="Impedanz")
plt.ylabel("$Z\;/\;$Ohm")
plt.xlabel("$f\,/\,kHz$")
plt.legend()
plt.savefig("build/plotZ.pdf",bbox_inches='tight')
plt.close()




# senkrechte Linie mit plt.axvline(x=5, ymin=0.1, ymax=0.9)