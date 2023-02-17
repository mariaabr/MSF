import numpy as np
import matplotlib.pyplot as plt

n = int((tf-t0)/dt)

t = np.linspace(t0, tf, n)
v = np.zeros(n) #or np.empty(n)

v[0] = v0
for i in range(n-1):
    v[i+1] = v[i] + g*dt
    
    
# metodo de euler para a e y também
a = np.zeros(n)
y = np.zeros(n)

a[0] = -g
v[0] = v0
for i in range(n-1):
    a[i+1] = - D*v[i]*np.abs(v[i]) - g
    v[i+1] = v[i] + a[i]*dt
    y[i+1] = y[i] + v[i]*dt
    
    
# calcular num determinado tempo (neste caso 3s e porque t é o nosso x)
for i in range(n-1):
    if ((t[i] > (3-dt) and t[i+1] < (3+dt))):
        print("dt, t, vy = ", dt, t[i+1], v[i+1])