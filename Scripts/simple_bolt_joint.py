# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 09:55:17 2016

@author: mauro
"""
"""
Proracun Steznog spoja

_____________________
Definiranje varijabli
_____________________
"""
r = 0.025  # Radijus cijevi [m]
l = 0.07  # Duzina spoja [m]

# Za vijak M12x1.75 klase 10.9 vrijedi:
M_v = 85.  # Moment pritezanja [Nm]
d_v = 0.012  # Promjer vijka [m]
mi_v = 0.2  # Faktor trenja navoja

F = 2000  # Sila [N]
k = 0.6  # Krak sile [m]
mi_stat = 0.15  # Statički koef trenja za spoj čelik-čelik
n = 2.  # Broj vijaka

"""
Proračun
________
"""
import math

A_c = r**2 * math.pi * l * 0.9  # Površina cilindra
F_va = M_v / (d_v * mi_v)  # Aksijalna sila u vijku

p_c = F_va / A_c  # Sila pritiska

M_c = (mi_stat * p_c * A_c) / 2.  # Moment proklizavanja za 1 vijak
M_c_uk = M_c * n

print('Nosivi moment : %d Nm, %d Kgm' % (M_c_uk, M_c_uk / 9.81))
