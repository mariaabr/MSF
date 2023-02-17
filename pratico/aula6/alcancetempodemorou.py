import matplotlib.pyplot as plt
import numpy as np

# g) o alcance e quanto tempo demorou

v0 = 1000/36
# x0 = 0
# y0 = 0
t0 = 0
tf = 1
dt = 0.001
g = 9.8
n = int((tf-t0)/dt)
vt = 1000/36
D = g/((vt)**2)

t = np.linspace(t0, tf, n)
vx = np.zeros(n) #or np.empty(n)
vy = np.zeros(n)
ax = np.zeros(n)
ay = np.zeros(n)
y = np.zeros(n)
x = np.zeros(n)
v = np.zeros(n)

vx[0] = v0 * np.cos(np.radians(10))
vy[0] = v0 * np.sin(np.radians(10))
# x[0] = x0
# y[0] = y0
for i in range(n-1):
    v[i] = np.sqrt(vy[i]**2 + vx[i]**2)
    ax[i] = - D*vx[i]*v[i]
    ay[i] = -g - D*vy[i]*v[i]
    vx[i+1] = vx[i] + ax[i]*dt
    vy[i+1] = vy[i] + ay[i]*dt
    y[i+1] = y[i] + vy[i]*dt
    x[i+1] = x[i] + vx[i]*dt
    
    # if y > 1 and y[i+1]*y[i] < 0:
    #     print(x)
    # CORRIGIR!!!

xanali = x[0]+vx[0]*t
yanali = y[0]+vy[0]*t-0.5*g*t**2
    
plt.plot(x, y, label = "lei do movimento")
plt.xlabel("t /(s)")
plt.ylabel("y /(m)")
plt.legend()
plt.plot(xanali, yanali, label = "y analítico")
plt.xlabel("t /(s)")
plt.ylabel("y /(m)")
plt.legend()