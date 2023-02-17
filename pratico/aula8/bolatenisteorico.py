import matplotlib.pyplot as plt
import numpy as np

# c)
v0 = 100/3.6
m = 0.057
teta = 10 #  0.1745 Radianos
dt = 0.001
t0 = 0
tf = 1
n = int((tf-t0)/dt)
g = 9.8
vt = 100/3.6
D = g/(vt**2)

t = np.linspace(t0, tf, n)
vx = np.zeros(n) # or np.empty(n)
vy = np.zeros(n)
ax = np.zeros(n)
ay = np.zeros(n)
x = np.zeros(n)
y = np.zeros(n)
v = np.zeros(n)
Em = np.zeros(n)

vx[0] = v0 * np.cos(np.radians(teta))
vy[0] = v0 * np.sin(np.radians(teta))
x[0] = 0
y[0] = 0

for i in range(n-1):
    v[i] = np.sqrt(vy[i]**2 + vx[i]**2)
    ax[i] = - D*vx[i]*v[i]
    ay[i] = -g - D*vy[i]*v[i]
    vx[i+1] = vx[i] + ax[i]*dt
    vy[i+1] = vy[i] + ay[i]*dt
    x[i+1] = x[i] + vx[i]*dt
    y[i+1] = y[i] + vy[i]*dt
    Em[i] = 0.5*m*v[i]**2 + m*g*y[i]

# definir o valor da Energia Mecânica do último ponto    
v[n - 1] = np.sqrt(vy[n - 1]**2 + vx[n - 1]**2)
Em[n -1] = 0.5*m*v[n - 1]**2 + m*g*y[n - 1]


# xanali = x[0]+vx[0]*t
# yanali = y[0]+vy[0]*t-0.5*g*t**2
    
    
plt.plot(t, Em)
plt.xlabel("t /(s)")
plt.ylabel("Em /(J)")