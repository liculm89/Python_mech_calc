# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 13:01:36 2015

@author: Mauro
"""

import math
import matplotlib.pyplot as plt
import numpy as np

"""
Definiranje konstanti i ulaznih parametara
"""

Fs = 1.5  # Faktor sigurnosti
# mi_0 = np.linspace(0.12, 0.4, 5)
# Statički koeficijent trenja (lijevano željezo - bronza P.CuSn 4)
mi_0 = 0.2
pcd = 0.080  # mm PCD The pitch-circle diametar - diametar na kojem su ravnomjerno raspoređeni vijci

# Geometrija spoja
r_out = 0.095  # mm Vanjski diametar dodirnih ploha
r_in = 0.065  # mm Unutarnji diametar dodirnih ploha

# Geometrija vijka - vijak s upuštenom glavom M6x1, L = 12 mm
d_v = 0.006  # mm promjer vijka (navoj)
d_gv = 0.012  # mm promjer vijka (glava vijka)
d_v_min = 0.00475  # mm korijen navoja  (min presjek)
v_gvs = 0.003  # mm visina glave vijka (stošca)
kut_v = 0.785398  # nagib glave upuštenog vijka (radijani)

n_vijaka = np.arange(2, 18, 2)

# mm duljina bočne stranice stošca
s = math.sqrt(v_gvs**2 + (d_gv / 2. - d_v / 2.)**2)
A_p = math.pi * ((d_gv / 2.)**2 + (d_v / 2.)**2 + (d_v + d_gv)
                 * s)  # mm^2 površina vijka u dodiru s plohom
# mm^2 poprečni presjek vijka, (za izračun naprezanja)
A_v = (d_v_min**2 * math.pi) / 4


# Definiranje naprezanja i momenta prednapregnutosti vijaka
klase = [8.8, 10.9, 12.9]
# Nm ... 9.5 - za vijak klase 8.8, 14.0 - vijak klase 10.9, 17.6 - vijak
# klase 12.9
M_pred = np.array([7.6, 10.3, 13.08])
# N/mm^2 ...640 - za vijak klase 8.8, 900 - vijak klase 10.9, 1080 - vijak
# klase 12.9
Sigma_rp02 = np.array([640., 900., 1080.])
Sigma_dop = np.zeros(len(M_pred))
Sigma_v = np.zeros(len(M_pred))
F_vaks = np.zeros(len(M_pred))  # Aksijalna sila u vijku
tau_max = np.zeros(len(M_pred))
F_tau = np.zeros(len(M_pred))


for i, m_p in enumerate(M_pred, start=0):
    # N/mm^2 Dopuštena naprezanja umanjena za faktor sigurnosti
    Sigma_dop[i] = Sigma_rp02[i] / Fs
    # N Aksijalna sila u vijku za različite klase vijaka
    F_vaks[i] = (m_p / (0.2 * d_v))
    # N/mm^2 Naprezanje u vijku za različe klase vijaka
    Sigma_v[i] = (F_vaks[i] / A_v) / 10**6
    # N/mm^2 Maksimalno dopušteno smično naprezanje (prema von Misesu)
    tau_max[i] = math.sqrt((Sigma_dop[i]**2 - Sigma_v[i]**2) / 3.)
    F_tau[i] = (tau_max[i] * A_v) * 10**6

"""
Maksimalni dozvoljeni moment ako se zanemari trenje
- proizlazi iz kriterija čvrstoće sigma_dop = sqrt (sigma_v**2 + tau_max**2 )
"""

Max_Load = np.zeros((len(n_vijaka), len(M_pred)))

for i, br_vijaka in enumerate(n_vijaka):
    for j, force_t in enumerate(F_tau):
        Max_Load[i][j] = force_t * br_vijaka * pcd / \
            2.  # Nm , maksimalni dozvoljeni moment

"""
Maksimalni dozvoljeni moment prenošen isključivo trenjem
"""
# Kako bi se izbjeglo smično naprezanje u vijcima, potrebno je osigurati
# dovoljnu silu za kompletan prijenos momenta trenjem

T_tr = np.zeros(len(M_pred))  # Moment trenja

for i, m_p in enumerate(M_pred):
    T_tr[i] = (2. / 3) * F_vaks[i] * mi_0 * (((r_out / 2.)**3 - \
               (r_in / 2.)**3) / ((r_out / 2.)**2 - (r_in / 2.)**2)) # Nm

Max_Tr_Load = np.zeros((len(n_vijaka), len(M_pred)))

for i, num in enumerate(n_vijaka):
    for j, force_t in enumerate(F_tau):
        Max_Tr_Load[i][j] = T_tr[j] * n_vijaka[i]

M_teret = np.arange(50, 3010, 10)  # Nm
F_teret = np.zeros(len(M_teret))
for i, m_t in enumerate(M_teret):
    # for i in range(len(M_teret)):
    F_teret[i] = m_t / (pcd / 2.)  # N

"""
Naprezanje u vijcima za poznati teret:  M_teret = arange(50,2510,50)
"""

Sigma_total = np.zeros((len(n_vijaka), len(M_pred), len(M_teret)))

for i, br_vijka in enumerate(n_vijaka):
    for j, m_p in enumerate(M_pred):
        for k, m_t in enumerate(M_teret):
            if (M_teret[k] >= Max_Tr_Load[i, j]):
                M_rez = M_teret[k] - Max_Tr_Load[i][j]
                F_rez_po_v = (M_rez / (pcd / 2.)) / n_vijaka[i]
                tau_po_v = (F_rez_po_v / A_v) / 10**6
                Sigma_ekv = math.sqrt((Sigma_v[j])**2 + tau_po_v**2)
                if (Sigma_ekv >= Sigma_dop[j]):
                    Sigma_total[i, j, k] = Sigma_v[j]
                else:
                    Sigma_total[i, j, k] = Sigma_ekv
            else:
                Sigma_total[i, j, k] = Sigma_v[j]

"""
Vizualizacija
"""
for i in range(len(M_pred)):
    plt.figure(i)
    plt.title(
        'Naprezanje u vijcima klase %s u ovisnosti o broju vijaka n ' %
        klase[i])
    for j in range(len(n_vijaka)):
        plt.plot(M_teret, Sigma_total[j, i, ])
        plt.legend(['n = 2', 'n = 4', 'n = 6', 'n = 8', 'n = 10',
                    'n = 12', 'n = 14', 'n = 16'], loc='upper left')
        plt.grid()
        plt.xlabel("Moment tereta [kNm]")
        plt.ylabel("Ekvivaletno naprezanje (prema Von Misesu) [MPa]")

plt.show()
