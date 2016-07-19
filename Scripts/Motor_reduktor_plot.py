# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 13:33:44 2016

@author: mauro
"""

"""
Određivanje redukcije i izlaznih performansi za pogon košarice

Motor: Dunkermotor BG 44 SI
"""
import numpy as np

N_nom = 2860  #rpm
T_nom = 5.7/100. #Nm 
N_min = 100 #rpm

T_const = 4.8/100. #Nm/A

Eta_reduktor = 0.8
#i_r = np.array()
i_arr = [14.,19.,25., 27., 46.,71.]
i_red = [14.,19.,25., 27., 46.,71.]
i_reduktor = 25
i_kosara = 3.2
i_total = i_reduktor * i_kosara
for i in range(len(i_arr)):
    i_arr[i] = i_arr[i]*i_kosara
N_kos_Nom = N_nom / i_total
T_kos_Nom = T_nom * i_total * Eta_reduktor

N_kos = np.linspace(0, 60 , 121)
N_motor_arr = []
for i in i_arr:
    N_motor_arr.append(N_kos*i)
 
N_motor = N_kos * i_total
N_m_1 = N_kos * i_arr[1]
import matplotlib
import matplotlib.pylab as plt
#from matplotlib import rc
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(18.5, 10.5, forward=True)
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

for item,num in enumerate(N_motor_arr):
    #print (num)
    plt.plot(N_kos, N_motor_arr[item], label='$i = %i*3.2$' % i_red[item])
#for i in range(len(N_motor_arr)):
#    plt.plot(N_kos, N_motor_arr[i], label='$i = %i*3.2$' % i_red[i])

plt.ylim(ymax = 7000, ymin = 0)
plt.minorticks_on()
plt.grid(b=True, which='major', color='k', linestyle='-')
plt.grid(b=True, which='minor', color='r', linestyle='--')
plt.title(r'\textbf{Brzina vrtnje kosarice za Intecno reduktore}')
plt.ylabel(r'\textbf{Brzina vrtnje motora} [o/min]')
plt.xlabel(r'\textbf{Brzina vrtnje kosarice} [o/min]')
plt.legend()
plt.show()