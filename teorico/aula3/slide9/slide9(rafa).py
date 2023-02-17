import numpy as np
import matplotlib.pyplot as plt
t0 = 0
x0 = 0
v0x = 0
n = 31
dt = 0.1
g = 9.81
t = np.linspace ( 0, n*dt, n )

def v(t):
    v = g*t
    return v

def x(t):
    x = 1/2*(g*(t**2))
    return x

v = v(t)
x = x(t)

plt.plot(t, v, label = "v(t)")
plt.plot(t, x, label = "x(t)")
plt.xlabel("t /(s)")
plt.ylabel("x(m) / v(m/s)")
plt.title("Posição do objeto :))")
plt.legend()