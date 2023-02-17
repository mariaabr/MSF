import matplotlib.pyplot as plt
import numpy as np

# 5c) bola de ténis batida junto ao solo com um ângulo de 10 graus com resistencia do ar - trabalho realizado
v0 = 1000/36
m = 0.057
teta = 10 #  0.1745 Radianos
vt = 1000/36

dt = 0.001
t0 = 0
tf = 1
n = int((tf-t0)/dt)
g = 9.8
D = g/(vt**2)

t = np.linspace(t0, tf, n)
vx = np.zeros(n) #or np.empty(n)
vy = np.zeros(n)
ax = np.zeros(n)
ay = np.zeros(n)
x = np.zeros(n)
y = np.zeros(n)
v = np.zeros(n)
Em = np.zeros(n)
fun = np.zeros(n)
trab = np.zeros(n)
aresy = np.zeros(n)

vx[0] = v0 * np.cos(np.radians(teta))
vy[0] = v0 * np.sin(np.radians(teta))
x[0] = 0
y[0] = 0

for i in range(n-1):
    v[i] = np.sqrt(vy[i]**2 + vx[i]**2)
    
    ax[i] = - D*vx[i]*v[i]
    ay[i] = -g - D*vy[i]*v[i]
    aresy[i] = - D*vy[i]*v[i]
    
    vx[i+1] = vx[i] + ax[i]*dt
    vy[i+1] = vy[i] + ay[i]*dt
    x[i+1] = x[i] + vx[i]*dt
    y[i+1] = y[i] + vy[i]*dt
    
# Método de Euler-Cromer:   
# for i in range(0, t.size-1):
#     rr = np.sqrt(Rx[i]**2 + Ry[i]**2)
#     Ax[i] = -g*m/rr**3*Rx[i]
#     Ay[i] = -g*m/rr**3*Ry[i]
#     Vx[i+1] = Vx[i] + Ax[i]*dt
#     Vy[i+1] = Vy[i] + Ay[i]*dt
#     Rx[i+1] = Rx[i] + Vx[i+1]*dt
#     Ry[i+1] = Ry[i] + Vy[i+1]*dt
    
    Em[i] = 0.5*m*v[i]**2 + m*g*y[i]
    fun[i] = m*ax[i]*vx[i] + m*aresy[i]*vy[i]
    trab[i] = dt*((fun[0] + fun[i])*0.5+np.sum(fun[1:i]))
    
#definir o valor da Energia Mecânica do último ponto    
v[n - 1] = np.sqrt(vy[n - 1]**2 + vx[n - 1]**2)
Em[n -1] = 0.5*m*v[n - 1]**2 + m*g*y[n - 1]
fun[n - 1] = m*ax[n - 1]*vx[n - 1] + m*ay[n - 1]*vy[n - 1]
# aproximação trapezoidal:
trab[n - 1] = dt*((fun[0] + fun[n - 1])*0.5+np.sum(fun[1:n - 1]))

for i in range(n-1):
    if (i == 0 ):
        print("dt, t, Trab = ", dt, t[i+1], trab[i])

for i in range(n-1):
    if (t[i] <= 0.4 < t[i+1]):
        print("dt, t, Trab = ", dt, t[i+1], trab[i])

for i in range(n-1):
    if ((t[i] > (0.8-dt) and t[i+1] <= (0.8+dt))):
        print("dt, t, Trab = ", dt, t[i+1], trab[i])

# plt.plot(x, y)
plt.plot(t, Em)
plt.xlabel("t /(s)")
plt.ylabel("Trab /(J)")
plt.grid()
