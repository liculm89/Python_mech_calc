# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 14:01:29 2016

#Izračun navojnog vretena

@author: mauro
"""
import math
# Dimenzije vretena
# Tip B+B+K Double preloaded nut in cube case

d_0 = 40.0   # Ddijametar vretena [mm]
P = 10.      # Korak [mm]
i = 3.       # Broj navoja matice
D_w = 6.35   # Dfijametar kugle [mm]

C_o = 87800  # Nominalno statičko opterećenje [N]
C_a = 36170  # Nominalno dinamičko opterećenje [N]

k = 173  # Faktor krutosti N/micro_m^(3/2)
R = 1009  # Aksijalna krutost N/micro_m

d_r = 34.0  # Dijametar korijena navoja [mm]
L_r = 825  # Radna dužina vretena [mm]
L_uk = 1025  # Udaljenst između ležajeva vretena [mm]
f_S = 3.


F_v = 0.1 * C_a  # N
f_v = 1.0  # Odabran prema
Q_kr = ((math.pi)**3 * 500 * d_0**4) / (f_v * L_uk**2)
F_a_max = Q_kr / 3.

print('Q_kr =', Q_kr)

print('F_amax =', F_a_max)

F_n = 4700
n_n = 350


L_1_2 = ((C_a * 1.25) / F_n)**3 * 10**6

print('L_1_2 = ', L_1_2)
"""
#Moment inercije
I_r = (math.pi * (d_r)**2) / 64.

#Modul elastičnosti
E = 210. # [GPa] = 1e-9 [N/mm**2]

L = 825. #hod vretena [mm]

lmbd = 2. # koeficijent rubnih uvjeta

F = lmbd * ((4. * (math.pi)**2) * ((210000 ) * I_r ))/(L**2)

P = 20. * (d_r**4/L**2) * 10**4

"""
