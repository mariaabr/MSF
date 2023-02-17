import matplotlib.pyplot as plt
import numpy as np

# Aula13 5 - Método de Runge-Kutta 4ªordem

# dados:
vt = 6.80
dt = 0.5
v0 = 0
x0 = 0
g = 9.8
t0 = 0
tf = 3
n = int((tf-t0)/dt)

def acelera(t,x,vx):
    ax = g - g/vt**2*np.abs(vx)*vx
    return ax

def rk4(t,x,vx,dt):

    ax1=acelera(t,x,vx)
    c1v=ax1*dt
    c1x=vx*dt
    ax2=acelera(t+dt/2.,x+c1x/2.,vx+c1v/2.)
    c2v=ax2*dt
    c2x=(vx+c1v/2.)*dt			# predicto:  vx(t+dt) * dt
    ax3=acelera(t+dt/2.,x+c2x/2.,vx+c2v/2.)
    c3v=ax3*dt
    c3x=(vx+c2v/2.)*dt
    ax4=acelera(t+dt,x+c3x,vx+c3v)
    c4v=ax4*dt
    c4x=(vx+c3v)*dt
      
    xp=x+(c1x+2.*c2x+2.*c3x+c4x)/6.
    vxp=vx+(c1v+2.*c2v+2.*c3v+c4v)/6.
    return xp,vxp

t = np.linspace(t0, tf, n)
vx = np.zeros(n) #or np.empty(n)
ax = np.zeros(n)
x = np.zeros(n)
vxrk4 = np.zeros(n)
xrk4 = np.zeros(n)

vx[0] = v0
x[0] = x0
vxrk4[0] = v0
xrk4[0] = x0

for i in range(n-1):
    # RK4
    xrk4[i+1], vxrk4[i+1] = rk4(t[i], xrk4[i], vxrk4[i],dt)
    # Euler - não é necessária, representa as diferenças entre o método rk4 e o método de euler
    ax[i] = acelera(t[i], x[i], vx[i])
    vx[i+1] = vx[i] + ax[i]*dt
    x[i+1] = x[i] + vx[i]*dt

plt.plot(t, vxrk4, label = "método RK4")
plt.plot(t, vx, label = "método de Euler")
plt.xlabel("t/(s)")
plt.ylabel("vx/(m/s)")
plt.legend()
plt.grid()






    
    
