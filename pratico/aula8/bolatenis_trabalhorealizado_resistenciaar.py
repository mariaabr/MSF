import matplotlib.pyplot as plt
import numpy as np

# c) trabalho realizado pela força de resistência do ar considerando a resistência do ar
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
aresx = np.zeros(n)
ay = np.zeros(n)
aresy = np.zeros(n)
x = np.zeros(n)
y = np.zeros(n)
v = np.zeros(n)
Em = np.zeros(n)
fun = np.zeros(n)
trab = np.zeros(n)

vx[0] = v0 * np.cos(np.radians(teta))
vy[0] = v0 * np.sin(np.radians(teta))
x[0] = 0
y[0] = 0

for i in range(n-1):
    v[i] = np.sqrt(vy[i]**2 + vx[i]**2)
    
    aresx[i] = - D*vx[i]*v[i]
    ax[i] = aresx[i]
    aresy[i] = - D*vy[i]*v[i]
    ay[i] = -g + aresy[i]
    
    vx[i+1] = vx[i] + ax[i]*dt
    vy[i+1] = vy[i] + ay[i]*dt
    
    x[i+1] = x[i] + vx[i]*dt
    y[i+1] = y[i] + vy[i]*dt
   
    Em[i] = 0.5*m*v[i]**2 + m*g*y[i]
    fun[i] = m*aresx[i]*vx[i] + m*aresy[i]*vy[i]
    trab[i] = dt*((fun[0] + fun[i])*0.5+np.sum(fun[1:i]))

#definir o valor da Energia Mecânica do último ponto    
v[n - 1] = np.sqrt(vy[n - 1]**2 + vx[n - 1]**2)
Em[n -1] = 0.5*m*v[n - 1]**2 + m*g*y[n - 1]
fun[n - 1] = m*aresx[n - 1]*vx[n - 1] + m*aresy[n - 1]*vy[n - 1]
trab[n - 1] = dt*((fun[0] + fun[n - 1])*0.5+np.sum(fun[1:n - 1]))

for i in range(n-1):
    if (i == 0 ):
        print("dt, t, Trab = ", dt, t[i+1], trab[i])

for i in range(n-1):
    if ((t[i] <= 0.4 < t[i+1])):
        print("dt, t, Trab = ", dt, t[i], trab[i])

for i in range(n-1):
    if ((t[i] > (0.8-dt) and t[i+1] <= (0.8+dt))):
        print("dt, t, Trab = ", dt, t[i+1], trab[i])
    
    
plt.plot(t, trab)
plt.xlabel("t /(s)")
plt.ylabel("Trab /(J)")
plt.grid()
