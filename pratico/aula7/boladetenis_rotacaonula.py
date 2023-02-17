import matplotlib.pyplot as plt
import numpy as np

# a) bola de ténis com rotação nula
v0 = 130/3.6
massabola = 0.057
teta = 10 #  0.1745 Radianos
diambola = 67*(10**(-3))
vt = 100/3.6
dt = 0.001
t0 = 0
tf = 1.4
n = int((tf-t0)/dt)
g = 9.8
D = g/(vt**2)

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

vx[0] = v0 * np.cos(np.radians(teta))
vy[0] = v0 * np.sin(np.radians(teta))
vz[0] = 0
x[0] = -10
y[0] = 1
z[0] = 0

for i in range(n-1):
    v[i] = np.sqrt(vy[i]**2 + vx[i]**2)
    ax[i] = - D*vx[i]*v[i]
    ay[i] = -g - D*vy[i]*v[i]
    az[i] = 0 
    vx[i+1] = vx[i] + ax[i]*dt
    vy[i+1] = vy[i] + ay[i]*dt
    vz[i+1] = vz[i] + az[i]*dt
    x[i+1] = x[i] + vx[i]*dt
    y[i+1] = y[i] + vy[i]*dt
    z[i+1] = z[i] + vz[i]*dt

for i in range(n-1):
    if (y[i+1]<y[i]):
        print("A altura max é {:0.2f} m".format(y[i+1]))
        plt.plot(x[i+1],y[i+1], "o", label="Altura máxima")
        break
    
for i in range(n-1):
    if (y[i+1]*y[i]<0):
        print("Alcance {:0.2f} m".format(x[i+1]))
        plt.plot(x[i+1],y[i+1], "o", label="Alcance")
        break

# print(np.max(x))
# print(np.max(y))
    
plt.plot(x, y)
# plt.plot(t, y)
# plt.plot(t, z)
plt.xlabel("x /(m)")
plt.ylabel("y /(m)")
plt.grid()

