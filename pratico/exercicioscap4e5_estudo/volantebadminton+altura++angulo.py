import matplotlib.pyplot as plt
import numpy as np

# 2a) e b) considerando a resistência do ar, altura em função da distância percorrida na horizontal

t0 = 0
tf = 1.75
dt = 0.001
g = 9.8
h = 3 #m
n = int((tf-t0)/dt)
v0 = 2000/36 # m/s
angulo = 10 # graus
vt = 6.80 #m/s
D = g/((vt)**2)


t = np.linspace(t0, tf, n)
vx = np.zeros(n) #or np.empty(n)
vy = np.zeros(n)
ax = np.zeros(n)
ay = np.zeros(n)
y = np.zeros(n)
x = np.zeros(n)
v = np.zeros(n)

vx[0] = v0 * np.cos(np.radians(angulo))
vy[0] = v0 * np.sin(np.radians(angulo))
x[0] = 0
y[0] = h

for i in range(n-1):
    v[i] = np.sqrt(vy[i]**2 + vx[i]**2) # norma de v através das suas coordenadas
    ax[i] = -D*v[i]*vx[i]
    ay[i] = -g - D*v[i]*vy[i]
    vx[i+1] = vx[i] + ax[i]*dt
    vy[i+1] = vy[i] + ay[i]*dt
    y[i+1] = y[i] + vy[i]*dt
    x[i+1] = x[i] + vx[i]*dt
    
# quando é que chegou ao chão e quanto tempo demorou, y = 0 m
for i in range (n-1):
    if y[i] > 0-dt and y[i+1] < 0+dt:
        print("Cai ao chão no ponto (m) no instante (s)(x,t):")
        print(x[i+1],";", t[i+1])


plt.plot(x, y, label = "altura em função da distância percorrida na horizontal")
plt.xlabel("x /(m)")
plt.ylabel("y /(m)")
plt.grid()
plt.legend()