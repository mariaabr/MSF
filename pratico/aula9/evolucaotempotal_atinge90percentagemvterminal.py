import matplotlib.pyplot as plt
import numpy as np

# Aaula9 ex12b - Empurrão inicial + descobrir a velocidade terminal
# b) 

v0 = 1 #m/s - empurrão inicial
m = 75
u = 0.004
Cres = 0.9
A = 0.3
p = 1.225
g = 9.8
P = 0.4*745.715
dt = 0.0001
t0 = 0
tf = 500
n = int((tf-t0)/dt)
tolerancia = 0.00001

t = np.linspace(t0, tf, n)
vx = np.zeros(n) # or np.empty(n)
ax = np.zeros(n)
x = np.zeros(n)
v = np.zeros(n)

vx[0] = v0
x[0] = 0
v[0] = v0

for i in range(n-1):
    v[i] = np.sqrt(vx[i]**2)
    ax[i] = u*g - (Cres/(2*m))*A*p*v[i]*vx[i] + P/(v[i]*m)
    vx[i+1] = vx[i] + ax[i]*dt
    x[i+1] = x[i] + vx[i]*dt

for i in range(n-1):
    if x[i] >= 2000:
        break
        print("Demorou {:0.2f} s".format(t[i]))
       

# plt.plot(t, v)
# plt.xlabel("t /(s)")
# plt.ylabel("v /(m/s)")