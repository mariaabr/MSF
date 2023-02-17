import matplotlib.pyplot as plt
import numpy as np

# 12a) Empurrão inicial + descobrir a velocidade terminal 

v0 = 1 #m/s - empurrão inicial
m = 75
u = 0.004
Cres = 0.9
A = 0.3
p = 1.225
g = 9.8
P = 0.4*745.715
dt = 0.0001
t0 = 0
tf = 60
n = int((tf-t0)/dt)
tolerancia = 0.0001

t = np.linspace(t0, tf, n)
vx = np.zeros(n) # or np.empty(n)
ax = np.zeros(n)
x = np.zeros(n)
v = np.zeros(n)

vx[0] = v0
ax[0] = 0
v[0] = v0

for i in range(n-1):
    v[i] = np.sqrt(vx[i] **2)
    ax[i] = -u*g - (Cres*A*p*v[i]*vx[i])/(2*m) + P/(m*v[i])

    vx[i+1] = vx[i] +ax[i]*dt  
    
    # definir o ponto em que a variação é praticamente nula    
    if vx[i+1]-vx[i] < tolerancia:
        print("vT = {:0.2f}".format(vx[i]))
        plt.plot(t[i],vx[i], "o",label="vT")
        break



# for i in range(n-1):    
#     if vx[i+1]-vx[i] < tolerancia:
#         print("vT = {:0.2f}".format(vx[i]))
#         plt.plot(t[i],vx[i], "o",label="vT")
#         break

v[n-1] = np.sqrt(vx[n-1]**2)
print("Velocidade terminal = ",v[n-1])
   
# vt = np.max(vx)
# print("vt = ", vt, "m/s")

plt.plot(t, v)
plt.xlabel("t /(s)")
plt.ylabel("v /(m/s)")
plt.grid()
plt.legend()