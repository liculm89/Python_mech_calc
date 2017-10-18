#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 13:16:37 2016

@author: Mauro
"""
# Proracun brzine konvejera
import math
from matplotlib import pyplot as plt
import numpy as np

n = 3000.

n_ovi = np.linspace(300, 10, 10)
for i in range(len(n_ovi)):
    n_ovi[i] = round(n_ovi[i], 1)

omege = np.zeros(len(n_ovi))
for i in range(len(omege)):
    omege[i] = ((math.pi * n_ovi[i]) / 30.)

omega = (math.pi * n) / 30

#print( 'omega iznosi: ', round(omega, 2))
radius = np.linspace(0.03, 0.06, 100)
# radiusi

brzine = np.zeros([len(n_ovi), len(radius)])

for i in range(len(n_ovi)):
    for j in range(len(radius)):
        brzine[i][j] = omege[i] * radius[j]

brzina = np.zeros(len(radius))

for i in range(len(radius)):
    brzina[i] = omega * radius[i]

radius = radius * 1000

fig = plt.figure()
# plt.figure(figsize=(19,12))
ax = fig.add_subplot(111)

ax.text(32, 2 - 0.5, r' $  \omega = \frac {\pi n}  {30}$', fontsize=25)
ax.text(32, 2 - 0.9, r' $v = \omega r$', fontsize=25)
import matplotlib as mpl
ax.get_xaxis().set_minor_locator(mpl.ticker.AutoMinorLocator())
ax.get_yaxis().set_minor_locator(mpl.ticker.AutoMinorLocator())
plt.grid(True, which='minor', color='black')
plt.grid(True, which='major', color='black')
#plt.plot(radius, brzina)
for i in range(len(brzine)):
    plt.plot(radius, brzine[i])
#n_ovi[:] = n_ovi[::-1]
plt.legend(n_ovi)
plt.title('Omjer radijusa i linearnog pomaka trake za n[okr/min]')
plt.xlim(30, 60)
plt.xlabel('Radijus trake [mm]')
plt.ylabel('Brzina trake [m/s]')
plt.show()
