#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 19:26:35 2022

@author: rafaela
"""
import numpy as np
import matplotlib.pyplot as plt
#aceleração gravítica
g =9.8

#velocidade inicial
v0 = 0.5 # para coonverter para m/s

u = 0.001
m = 60 + 12
Cres = 0.9
Af = 0.50
densidade_ar= 1.225

#Tmpo inicial e final
ti =0
tf = 200
dt = 0.001
n = int((tf-ti) / dt)


#Arrays precisam de ser todos definidos
t = np.linspace(ti, tf, n)

v = np.empty(n)
vx = np.empty(n)
ax = np.empty(n)
x = np.empty(n)

vx[0] = v0
v[0] = v0
ax[0] = 0
x[0] = 0
tolerancia = 0.00001

P = 0.48 * 745.698872

for i in range(n-1):
    v[i] = np.sqrt(vx[i] **2)
    ax[i] = -u*g - (Cres*Af*densidade_ar*v[i]*vx[i])/(2*m) + P/(m*v[i])
    vx[i+1] = vx[i] +ax[i]*dt
    x[i+1] = x[i] + vx[i]*dt
    
for i in range(n-1):
    if x[i+1] > 2000:
        print("km percorridos", x[i + 1])
        print("demorou:", t[i + 1])
        break
    
v[n-1] = np.sqrt(vx[n-1]**2)

plt.plot(t ,v)
plt.xlabel("t (s) ")
plt.ylabel("v (m/s)")
plt.title("evolução temporal ")
plt.grid()