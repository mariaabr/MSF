import matplotlib.pyplot as plt
import numpy as np


# 3 considerando a resistência do ar, altura em função da distância percorrida na horizontal
# fazer o produto vetorial à parte e ver qual do x,y ou z é que se elimina ---> ir trocando algumas incógnitas planeadas, as que não forem eliminadas

t0 = 0
tf = 0.5
dt = 0.001
n = int((tf-t0)/dt)
g = 9.8
m = 0.45 #kg
r = 0.11 #m
angulo = 10 #graus
omega = 400
vt = 1000/36 #m/s
D = g/((vt)**2)
den = 1.225
area = np.pi*r**2
mag = 0.5*den*area*r/m


t = np.linspace(t0, tf, n)
vx = np.zeros(n) #or np.empty(n)
vy = np.zeros(n)
vz = np.zeros(n)
ax = np.zeros(n)
ay = np.zeros(n)
az = np.zeros(n)
x = np.zeros(n)
y = np.zeros(n)
z = np.zeros(n)
v = np.zeros(n)

vx[0] = 25
vy[0] = 5
vz[0] = -50
x[0] = 0
y[0] = 0
z[0] = 23.8

for i in range(n-1):
    v[i] = np.sqrt(vx[i]**2 + vz[i]**2)
    Fmx = mag*omega*vz[i]
    Fmz = -mag*omega*vx[i]
    ax[i] = - D*vx[i]*v[i] + Fmx
    ay[i] = -g - D*vy[i]*v[i]
    az[i] = - D*vz[i]*v[i] + Fmz
    vx[i+1] = vx[i] + ax[i]*dt
    vy[i+1] = vy[i] + ay[i]*dt
    vz[i+1] = vz[i] + az[i]*dt
    x[i+1] = x[i] + vx[i]*dt
    y[i+1] = y[i] + vy[i]*dt
    z[i+1] = z[i] + vz[i]*dt

for i in range(n-1):
    if x[i] < 0 and 0 < z[i] < 7.3 and 0 < y[i] < 2.4:
        print("É GOLOOO!!!")
        print("(x,y,z)", x[i],";", y[i],";", z[i])

plt.plot(t, x, label = "x(t)")
plt.xlabel("t /(s)")
plt.ylabel("x /(m)")
plt.grid()
plt.plot(t, y, label = "y(t)")
plt.ylabel("y /(m)")
plt.plot(t, z, label = "z(t)")
plt.ylabel("z /(m)")
plt.legend()