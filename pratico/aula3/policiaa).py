import matplotlib.pyplot as plt
import numpy as np

# a)
x0c = 0
x0p = 0
v0p = 0
vkmh = 700
vc = vkmh/36 #m/s
ac = 0
ap = 2

t = np.linspace(0,25,100)

xc = vc*t 
xp = t*t


plt.plot(t, xp, label = "x(t) carro polícia")
plt.plot(t, xc, label = "x(t) carro")
plt.xlabel("t /(s)")
plt.ylabel("x(m)")
plt.title("Posição do carro :))")
plt.legend()




# lia
# import numpy as np
# import matplotlib.pyplot as plt

# x0c = 0 
# x0p = 0
# v0c = 700/36
# v0p = 0
# ac = 0
# ap = 2

# t = np.linspace(0,25,100)
# xtc = v0c * t
# xtp = tt

# plt.plot(t,xtc,label="X(t) do carro")
# plt.plot(t,xtp,label="X(t) da polícia")
# plt.xlabel("t /(s)")
# plt.ylabel("x/(m)")
# plt.legend()
# plt.show()

# tintersect = v0c
# xintersect = v0cv0c
# print("T = {} s, X= {} m".format(tintersect,xintersect))