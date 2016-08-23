# -*- coding: utf-8 -*-
"""
Created on Mon Jun 08 08:50:54 2015

@author: Mauro
"""

# Proračun sile opruge
# č. 1630
E = 2.1 * 10**5  # Moduli elastičnosti

Rm = 1500.  # Vlačna čvrstoća
R_p02 = 1300.
ni = 0.3
G = E / (2 + (1 + ni))

D = 13.0  # promjer opruge [mm]
d = 1.5  # promjer žice [mm]

L_0 = 20.  # Visina opuštene opruge
L_c = 15.  # visina napregnute opruge [mm]

#razlika, s = abs(v_o - v_n)
s = abs(L_0 - L_c)

# korak
k = 5.

# broj zavoja opruge
n = L_0 / k
s_tmax = L_0 - (n * d)

# sila opruge
F = (G / 8.) * (d**4 / D**3) * (s / n)

# max_sila
F_max = (G / 8.) * (d**4 / D**3) * (s_tmax / n)

print("Sila opruge za skraćenje %d mm:" % s, round(F,3), "N")
print("Sila opruge za skraćenje %d mm:" % s_tmax, round(F_max,3), "N")
