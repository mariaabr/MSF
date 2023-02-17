import matplotlib.pyplot as plt
import numpy as np

# Aula12 - 10 calcular o período do movimento

t0 = 0
tf = 20
dt = 0.001
g = 9.8
n = int((tf-t0)/dt)
angulo = 10 # graus
L = 1
teta0 = 30

t = np.linspace(t0, tf, n)
# vx = np.zeros(n) #or np.empty(n)
# vy = np.zeros(n)
ax = np.zeros(n)
# ay = np.zeros(n)
# y = np.zeros(n)
teta = np.zeros(n)
w = np.zeros(n)

w[0] = 0
teta[0] = np.radians(teta0)

for i in range(n-1):
    ax[i] = -(g/L)*np.sin(teta[i])
    w[i+1] = w[i] + ax[i]*dt
    teta[i+1] = teta[i] + w[i+1]*dt
    
tempos = []
periodos = []
       
for i in range(n-1):
    if (teta[i-1] < teta[i] > teta[i+1] and i > 0):
        tempos.append(t[i])
        
        
for i in range(1, len(tempos)-1):
    temp = tempos[i+1] - tempos[i]
    periodos.append(temp)
      
T = sum(periodos)/(len(periodos)) 
print(T)
print("O valor aproximado da amplitude é: {:.4f}".format(T), "s")

plt.plot(t, np.degrees(teta))
plt.xlabel("t /(s)")
plt.ylabel("teta /(º)")
plt.grid()