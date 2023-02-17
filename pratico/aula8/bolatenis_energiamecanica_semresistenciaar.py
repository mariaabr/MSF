import matplotlib.pyplot as plt
import numpy as np

# Aula8 ex3a - bola de ténis lançada a partir do solo sem resistência do
# ar com velocidade inicial igual a 100 kmm/h e um ângulo de 10 graus
# a)
v0 = 100/3.6
teta = 10 #  0.1745 Radianos
dt = 0.001
t0 = 0
tf = 1
n = int((tf-t0)/dt)
g = 9.8
m = 0.057
# Ecin = (1/2)*m*v**2
# Epot = m*g*h
# Emecan = Ecin + Epot

t = np.linspace(t0, tf, n)

vx = np.zeros(n) #or np.empty(n)
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

    ax[i] = 0
    ay[i] = -g
    vx[i+1] = vx[i] + ax[i]*dt
    vy[i+1] = vy[i] + ay[i]*dt
    v[i] = np.sqrt(vy[i]**2 + vx[i]**2)
    x[i+1] = x[i] + vx[i]*dt
    y[i+1] = y[i] + vy[i]*dt
    
    Em[i] = 0.5*m*v[i]**2 + m*g*y[i]

#definir o valor da Energia Mecânica do último ponto    
v[n - 1] = np.sqrt(vy[n - 1]**2 + vx[n - 1]**2)
Em[n -1] = 0.5*m*v[n - 1]**2 + m*g*y[n - 1]
    
# plt.plot(x, y)
plt.plot(t, Em)
plt.xlabel("t /(s)")
plt.ylabel("Em /(J)")
plt.grid()