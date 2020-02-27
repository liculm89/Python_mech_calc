# -*- coding: utf-8 -*-
"""
@author: mauro
"""
import math

C = 1.15
ro = 1.22  # kg/m^3

side_a = 0.05  # m
side_b = 0.05  # m

A = side_a * side_b

velocity = 40  # m/s
# Force calculation

F_d = 1/2 * C * ro * A * math.pow(velocity, 2)

print("F = ", F_d, "N")
