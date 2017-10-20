# -*- coding: utf-8 -*-
"""
Created on Mon Jun 08 08:50:54 2015

@author: Mauro
"""

# Proračun sile opruge
# č. 1630
import numpy as np
import matplotlib.pyplot as plt

E = 2.1 * 10**5  # Moduli elastičnosti

Rm = 1500.  # Vlačna čvrstoća
R_p02 = 1300.
ni = 0.3
G = E / (2 + (1 + ni))

D = 11.5  # promjer opruge [mm]
d = 1.0 # promjer žice [mm]

L_0 = 40.  # Visina opuštene opruge
L_c = 19.  # visina napregnute opruge [mm]


#razlika, s = abs(v_o - v_n)
s = abs(L_0 - L_c)

# korak
k = 5.

# broj zavoja opruge
n = L_0 / k
s_tmax = L_0 - (n * d)
X = np.linspace(0, s_tmax - 1, num=10)
Y = np.zeros(len(X))
for i in range(len(X)):
    Y[i] = (G / 8.) * (d**4 / D**3) * (X[i] / n)
# sila opruge
F = (G / 8.) * (d**4 / D**3) * (s / n)

# max_sila
F_max = (G / 8.) * (d**4 / D**3) * (s_tmax / n)

print(X);
print(Y);
print("Sila opruge za skraćenje %d mm:" % s, round(F,2), "N")
print("Sila opruge za skraćenje %d mm:" % s_tmax, round(F_max,2), "N")

fig = plt.figure()

fig.suptitle('Grafe sile/skraćenja za opruge')
plt.xlabel('Skraćenje opruge (mm)')
plt.ylabel('Sila opruge (N)')
plt.grid()
plt.plot(X,Y)
plt.show()