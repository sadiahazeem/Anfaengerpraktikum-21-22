import matplotlib.pyplot as plt
import numpy as np

x_messing_500, dm_messing_500 = np.genfromtxt('./content/MessingRund500gEinseitig.txt', delimiter=",", skip_header=True, unpack=True)
x_messing, d0_messing = np.genfromtxt('./content/MessingRundD0Einseitig.txt', delimiter=",", skip_header=True, unpack=True)
x_alu_500, dm_alu_500 = np.genfromtxt('./content/AluEckig500gEinseitig.txt', delimiter=",", skip_header=True, unpack=True)
x_alu, d0_alu = np.genfromtxt('./content/AluEckigD0Einseitig.txt', delimiter=",", skip_header=True, unpack=True)

# Length of rod
L_mm = 550

# Regression of messing measurements for dm
x_temp_500 = L_mm*x_messing_500**2 - x_messing_500**3/3
model_500 = np.polyfit(x_temp_500, dm_messing_500, 1)
predict_500 = np.poly1d(model_500)
y_temp_500 = predict_500(x_temp_500)
print(model_500)
# Regression of messing measurements for d0
x_temp = L_mm*x_messing**2 - x_messing**3/3
model = np.polyfit(x_temp, d0_messing, 1)
predict = np.poly1d(model)
y_temp = predict(x_temp)
print(model)
# Linspace for y_ready values
x = np.linspace(30, 470, 30)
x_weird = L_mm*x**2 - x**3/3

# Substract interpolated y values -> d_m - d0
y_ready = predict_500(x_weird) - predict(x)

plt.figure()
plt.grid(True)
plt.plot(x_temp_500, y_temp_500, label=r'Ausgleichsgerade $D_m$', color='r')
plt.scatter(x_temp_500, y_temp_500, label=r'Messwerte $D_m$', color='b')
plt.plot(x_temp, y_temp, label=r'Ausgleichsgerade $D_0$', color='r', linestyle='dashed')
plt.scatter(x_temp, y_temp, label=r'Messwerte $D_0$', color='b', linestyle='dashed')
plt.plot(x_weird, y_ready, label=r'Ausgleichsgerade für $\Delta D = D_m - D_0$', color='g')
plt.xlabel(r'$Lx^2 - \frac{x^3}{3} \mathbin{/} \unit{\mm\cubed}$')
plt.ylabel(r'$D(x) \mathbin{/} \unit{\mm}$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot_messing_einseitig.pdf')


# Regression of messing measurements for dm
x_temp_500 = L_mm*x_alu_500**2 - x_alu_500**3/3
model_500 = np.polyfit(x_temp_500, dm_alu_500, 1)
predict_500 = np.poly1d(model_500)
y_temp_500 = predict_500(x_temp_500)
print(model_500)
# Regression of messing measurements for d0
x_temp = L_mm*x_alu**2 - x_alu**3/3
model = np.polyfit(x_temp, d0_alu, 1)
predict = np.poly1d(model)
y_temp = predict(x_temp)
print(model)
# Linspace for y_ready values
x = np.linspace(30, 470, 30)
x_weird = L_mm*x**2 - x**3/3

# Substract interpolated y values -> d_m - d0
y_ready = predict_500(x_weird) - predict(x)

plt.figure()
plt.grid(True)
plt.plot(x_temp_500, y_temp_500, label=r'Ausgleichsgerade $D_m$', color='r')
plt.scatter(x_temp_500, y_temp_500, label=r'Messwerte $D_m$', color='b')
plt.plot(x_temp, y_temp, label=r'Ausgleichsgerade $D_0$', color='r', linestyle='dashed')
plt.scatter(x_temp, y_temp, label=r'Messwerte $D_0$', color='b', linestyle='dashed')
plt.plot(x_weird, y_ready, label=r'Ausgleichsgerade für $\Delta D = D_m - D_0$', color='g')
plt.xlabel(r'$Lx^2 - \frac{x^3}{3} \mathbin{/} \unit{\mm\cubed}$')
plt.ylabel(r'$D(x) \mathbin{/} \unit{\mm}$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot_alu_einseitig.pdf')


x_rechts, d0_rechts, dm_rechts = np.genfromtxt('./content/messing_beidseitig_rechts.txt', delimiter=",", skip_header=True, unpack=True)
x_links, d0_links, dm_links = np.genfromtxt('./content/messing_beidseitig_links.txt', delimiter=",", skip_header=True, unpack=True)

x_rechts_temp = 3*x_rechts*L_mm**2 - 4*x_rechts**3
y_rechts_temp = dm_rechts - d0_rechts

x_links_temp = 3*x_links*L_mm**2 - 4*x_links**3
y_links_temp = dm_links - d0_links

model_rechts = np.polyfit(x_rechts_temp, y_rechts_temp, 1)
model_links = np.polyfit(x_links_temp, y_links_temp, 1)
print(model_rechts)
print(model_links)

predict_rechts = np.poly1d(model_rechts)
y_rechts = predict_rechts(x_rechts_temp)

predict_links = np.poly1d(model_links)
y_links = predict_links(x_links_temp)

plt.figure()
plt.grid(True)
plt.plot(x_rechts_temp, y_rechts, label='Ausgleichsgerade', color='r', linestyle='dashed')
plt.scatter(x_rechts_temp, y_rechts, label='Messwerte', color='b')
plt.xlabel(r'$3L^2x - 4x^3 \mathbin{/} \unit{\mm\cubed}$')
plt.ylabel(r'$D(x) \mathbin{/} \unit{\mm}$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot_beidseitig_rechts.pdf')


plt.figure()
plt.grid(True)
plt.plot(x_links_temp, y_links, label='Ausgleichsgerade', color='r', linestyle='dashed')
plt.scatter(x_links_temp, y_links, label='Messwerte', color='b')
plt.xlabel(r'$3L^2x - 4x^3 \mathbin{/} \unit{\mm\cubed}$')
plt.ylabel(r'$D(x) \mathbin{/} \unit{\mm}$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot_beidseitig_links.pdf')

