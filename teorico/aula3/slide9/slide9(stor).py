import numpy as np
import matplotlib.pyplot as plt

dt = 0.01
# tf = 4.0
t0 = 0
x0 = 0
g = 9.80
v0x = 0
n = 100

t = np.linspace ( 0, n*dt, n )
#Aproxiamtion = [0]*(N+1) #[0, 0, 0, ..., 0N]

vx = []
t = []
x = []

vx.append(v0x)
t.append(t0)
x.append(x0)
print(vx[0])
i=0
while i < n: # Método de Euler
    r=t[i]+dt    
    t.append(r)
    vxT = g*(i+1)*dt
    vx.append(vxT)
    m=x[i]+(vx[i])*dt
    x.append(m)
    i=i+1
    
plt.plot(t, x, "x")
plt.xlabel("t /(s)")
plt.ylabel("x(m) / v(m/s)")
plt.title("Posição do objeto :))")
plt.legend()