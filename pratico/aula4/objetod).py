import matplotlib.pyplot as plt
import numpy as np

# d)
v0 = 0
y0 = 0
t0 = 0
tf = 3
dt = 0.01
g = -9.8
n = int((tf-t0)/dt)

t = np.linspace(t0, tf, n)
v = np.zeros(n) #or np.empty(n)
y = np.empty(n)

v[0] = v0
y[0] =y0
for i in range(n-1):
    v[i+1] = v[i] + g*dt
    y[i+1] = y[i] + v[i]*dt
    
for i in range(n-1):
    if ((t[i] > (2-dt) and t[i+1] < (2+dt))):
        print("dt, t, vy = ", dt, t[i+1], y[i+1])

    
plt.plot(t, y, label = "x(t)")
plt.xlabel("t /(s)")
plt.ylabel("x /(m)")
plt.legend()