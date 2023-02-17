import matplotlib.pyplot as plt
import numpy as np

# c)

v0 = 0
t0 = 0
tf = 4
dt = 0.001
g = -9.8
n = int((tf-t0)/dt)

t = np.linspace(t0, tf, n)
v = np.zeros(n) #or np.empty(n)

v[0] = v0
for i in range(n-1):
    v[i+1] = v[i] + g*dt
    
for i in range(n-1):
    if ((t[i] > (3-dt) and t[i+1] < (3+dt))):
        print("dt, t, vy = ", dt, t[i+1], v[i+1])

plt.plot(t, v, label = "a(t)")
plt.xlabel("t /(s)")
plt.ylabel("v /(m/s)")
plt.legend()