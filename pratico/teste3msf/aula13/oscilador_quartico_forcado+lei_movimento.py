import matplotlib.pyplot as plt
import numpy as np

# Aula13 4 -Oscilador quártico forçado + lei do movimento + amplitude e período
# a) e b)


v0 = 0
m = 1
k = 1
x0 = 4
b = 0.05
alpha = 0.002
F0 = 7.5
w = 1

dt = 0.001
t0 = 0
tf = 400
n = int((tf-t0)/dt)
g = 9.8

t = np.linspace(t0, tf, n)
vx = np.zeros(n) #or np.empty(n)
ax = np.zeros(n)
x = np.zeros(n)
v = np.zeros(n)

vx[0] = v0
x[0] = x0

# método de euler-cromer:
for i in range(n-1):
    ax[i] = -(k/m)*x[i]*(1 + 2*alpha*(x[i]**2)) - (b/m)*vx[i] + (F0/m)*np.cos(w*t[i])
    vx[i+1] = vx[i] + ax[i]*dt
    x[i+1] = x[i] + vx[i+1]*dt
    

#Amplitude/Periodo
Amax = []

tempos = []
periodos = []
       
for i in range(n-1):
    if (x[i-1] < x[i] > x[i+1] and t[i] > 200):
        Amax.append(x[i])
        tempos.append(t[i])
        
        
for i in range(1, len(tempos)-1):
    temp = tempos[i+1] - tempos[i]
    periodos.append(temp)
    
    
A = sum(Amax)/(len(Amax))       
T = sum(periodos)/(len(periodos))    

#PRINTS
        
print(Amax)
print(periodos)

print("O valor aproximado da amplitude é: {:.4f}".format(A), "m")

print("O valor aproximado da amplitude é: {:.4f}".format(T), "s")

    
plt.plot(t, x)
plt.xlabel("t /(s))")
plt.ylabel("x /(m)")
plt.grid()