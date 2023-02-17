import matplotlib.pyplot as plt
import numpy as np

# b)
v0 = 0
t0 = 0
tf = 4
dt = 0.1
g = -9.8
n = int((tf-t0)/dt)

t = np.linspace(t0, tf, n)
v = np.zeros(n) #or np.empty(n)

v[0] = v0
for i in range(n-1):
    v[i+1] = v[i] + g*dt

    
    
plt.plot(t, v, label = "a(t)")
plt.xlabel("t /(s)")
plt.ylabel("v /(m/s)")
plt.legend()
