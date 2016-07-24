#! /usr/bin/python3
# coding: utf-8
"""
Created on Sat Mar 26 13:33:44 2016

@author: mauro
"""

"""
Određivanje redukcije i izlaznih performansi za pogon košarice

Motor: Dunkermotor BG 44 SI
"""
import numpy as np

N_NOM = 2860  # rpm
T_NOM = 5.7 / 100.0
N_MIN = 100  # rpm

T_const = 4.8 / 100.  # Nm/A

Eta_reduktor = 0.8
#i_r = np.array()
I_ARR = [14., 19., 25., 27., 46., 71.]
I_RED = [14., 19., 25., 27., 46., 71.]
I_REDUKTOR = 25
I_KOSARA = 3.2
I_TOTAL = I_REDUKTOR * I_KOSARA
for i in range(len(I_ARR)):
    I_ARR[i] = I_ARR[i] * I_KOSARA
N_KOS_Nom = N_NOM / I_TOTAL
T_kos_Nom = T_NOM * I_TOTAL * Eta_reduktor

N_KOS = np.linspace(0, 60, 121)
N_motor_arr = []
for i in I_ARR:
    N_motor_arr.append(N_KOS * i)

N_motor = N_KOS * I_TOTAL
N_m_1 = N_KOS * I_ARR[1]
import matplotlib
import matplotlib.pylab as plt
#from matplotlib import rc
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(18.5, 10.5, forward=True)
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

for item, num in enumerate(N_motor_arr):
    #print (num)
    plt.plot(N_KOS, N_motor_arr[item], label='$i = %i*3.2$' % I_RED[item])
# for i in range(len(N_motor_arr)):
#    plt.plot(N_KOS, N_motor_arr[i], label='$i = %i*3.2$' % I_RED[i])

plt.ylim(ymax=7000, ymin=0)
plt.minorticks_on()
plt.grid(b=True, which='major', color='k', linestyle='-')
plt.grid(b=True, which='minor', color='r', linestyle='--')
plt.title(r'\textbf{Brzina vrtnje kosarice za Intecno reduktore}')
plt.ylabel(r'\textbf{Brzina vrtnje motora} [o/min]')
plt.xlabel(r'\textbf{Brzina vrtnje kosarice} [o/min]')
plt.legend()
plt.show()
