import matplotlib.pyplot as plt
import numpy as np

# 9a) - Potência do movimento de um ciclista 

v0 = 30/3.6 #m/s
m = 75
u = 0.004
Cres = 0.9
A = 0.3
p = 1.225
g = 9.8
vx = 30/3.6

P =(u*m*g*v0 + (Cres/2)*A*p*(v0**2))*vx
print(P)