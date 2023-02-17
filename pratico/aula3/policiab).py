import matplotlib.pyplot as plt
import numpy as np

x0c = 0
x0p = 0
v0p = 0
vkmh = 700
vc = vkmh/36 #m/s
ac = 0
ap = 2.0

t = np.linspace(0,25,100)

xc = vc*t 
xp = t*t


plt.plot(t, xp, label = "x(t) carro polícia")
plt.plot(t, xc, label = "x(t) carro")
plt.xlabel("t /(s)")
plt.ylabel("x(m)")
plt.title("Posição do carro :))")
plt.legend()

# b)

tintersect = vc
xintersect = vc*vc
print("T = {:.1f} s; X= {:.1f} m".format(tintersect,xintersect))