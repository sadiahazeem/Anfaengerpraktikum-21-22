import matplotlib.pyplot as plt
import numpy as np

t, T1, T2, T3, T4, T5, T6, T7, T8 = np.genfromtxt('StatischeMessung.txt', encoding="utf-16" ,unpack=True)
t *= 5

Tst1 = T7 - T8
Tst2 = T2 - T1

#Plot der Temperaturverlaeufe von T1, T4, T5 und T8
plt.figure()
plt.plot(t, T1, label='T1(Messing breit)')
plt.plot(t, T4, label='T4(Messing schmal)')
plt.plot(t, T5, label='T5(Aluminium)')
plt.plot(t, T8, label='T8(Edelstahl)')
plt.grid(True, linewidth=0.5)
plt.xlabel(r'$t \mathbin{/} \unit{\second}$')
plt.ylabel(r'$T \mathbin{/} \unit{\celsius}$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot1.pdf')


#Plot der Differenz von T7 und T8 und von T2 und T1
plt.figure()
plt.plot(t, Tst1, label='T7 - T8')
plt.plot(t, Tst2, label='T2 - T1')
plt.grid(True, linewidth=0.5)
plt.xlabel(r'$t \mathbin{/} \unit{\second}$')
plt.ylabel(r'$T \mathbin{/} \unit{\celsius}$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot2.pdf')

t, T1, T2, T3, T4, T5, T6, T7, T8 = np.genfromtxt('DynamischeMessung40s.txt', encoding="utf-16" ,unpack=True)
t *= 2

#Plot fuer die Temperaturwelle von Messing(breit) bei 80s Periodendauer
plt.figure()
plt.plot(t, T1, label=r'$T_{fern}$')
plt.plot(t, T2, label=r'$T_{nah}$')
plt.grid(True, linewidth=0.5)
plt.xlabel(r'$t \mathbin{/} \unit{\second}$')
plt.ylabel(r'$T \mathbin{/} \unit{\celsius}$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot3.pdf')


#Plot fuer die Temperaturwelle von Aluminium bei 80s Periodendauer
plt.figure()
plt.plot(t, T5, label=r'$T_{fern}$')
plt.plot(t, T6, label=r'$T_{nah}$')
plt.grid(True, linewidth=0.5)
plt.xlabel(r'$t \mathbin{/} \unit{\second}$')
plt.ylabel(r'$T \mathbin{/} \unit{\celsius}$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot4.pdf')