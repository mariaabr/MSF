import matplotlib.pyplot as plt
import numpy as np

t0 = 0
tf = 10
x0 = 0
v0p = 0
a = 2
vkmh = 70
vc = vkmh/3,6 #m/s
np = 100

t = np.linspace ( 0, 10, 100 )

x = vc*t 
xp = t*t


plt.plot(t, xp, label = "v carro polícia")
plt.plot(t, x, label = "v carro")
plt.xlabel("t /(s)")
plt.ylabel("x(m)")
plt.title("Posição do carro :))")
plt.legend()

