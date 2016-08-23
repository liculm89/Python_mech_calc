# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 10:16:20 2015

@author: Mauro
"""
import math as math
import numpy as np

fi_cilindricni = 24.  # mm
fi_konus = 30.  # mm
tlak = 80  # bar

tlak = np.arange(1, 100, 5)

A_cil = (fi_cilindricni**2 * math.pi) / 4.
A_konus = ((fi_konus**2 * math.pi) / 4 - A_cil) * math.cos(math.radians(45))
A = A_cil + A_konus


F = (tlak * 10**5) * A * 10**(-6)

import matplotlib.pyplot as plt

plt.figure(1)
plt.title("Karakteristika hidraulicne vage (tlak/sila)")
plt.xlabel("Tlak P [bar]")
plt.ylabel("Sila F [N]")
plt.grid()
plt.plot(tlak, F)

G = F / 9.81

plt.figure(2)
plt.title("Karakteristika hidraulicne vage (tlak/tezina)")
plt.xlabel("Tlak P [bar]")
plt.ylabel("Tezina G [kg]")
plt.grid()
plt.plot(tlak, G)


plt.show()
