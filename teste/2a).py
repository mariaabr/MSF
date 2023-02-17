import matplotlib.pyplot as plt
import numpy as np

# a)
v0 = 0
t0 = 0
y0 = 800
tf = 4
dt = 0.001
g = -9.8
n = int((tf-t0)/dt)

t = np.linspace(0, 1000, n)
v = np.zeros(n) #or np.empty(n)
y = np.zeros(n)

v[0] = v0
y[0] = y0
for i in range(n-1):
    v[i+1] = v[i] + g*dt
    y[i+1] = y[i] + v[i]*dt

    
    
plt.plot(t, y, label = "v(t)")
plt.xlabel("t /(s)")
plt.ylabel("y /(m)")
plt.legend()
