import matplotlib.pyplot as plt
import numpy as np

# d)

v0 = 10
y0 = 0
dt = 0.001
g = 9.8
vt = 100/3.6

D = g/((vt)**2)


tf=2.2
t0=0
n=int((tf-t0)/dt)

t = np.linspace(t0, tf, n)
v = np.zeros(n) #or np.empty(n)
a = np.zeros(n)
y = np.zeros(n)

a[0] = -g
v[0] = v0
for i in range(n-1):
    a[i+1] = - D*v[i]*np.abs(v[i]) - g
    v[i+1] = v[i] + a[i]*dt
    y[i+1] = y[i] + v[i]*dt
    
# calcular altura máxima
for i in range(n):
    if v[i] > 0-dt and v[i+1] < 0+dt:
        print("Altura máxima com resistência do ar (t,v,y(m/s),v(km/h):")
        print(t[i+1],y[i+1],v[i+1],v[i+1]*3600/1000)

# voltar a passar na posição inicial
for i in range(n-1):
    if y[i] > 0-dt and y[i+1] < 0+dt:
        print("Regresso à posição inicial (t,v,y(m/s),v(km/h):")
        print(t[i+1],y[i+1],v[i+1],v[i+1]*3600/1000)
    
    
# plt.plot(t, a, label = "a(t)")  
# plt.plot(t, v, label = "v(t)")
plt.plot(t, y, label = "y(t)")
plt.xlabel("t /(s)")
plt.xlabel("y /(m)")
plt.legend()