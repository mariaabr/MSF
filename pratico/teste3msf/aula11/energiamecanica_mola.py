import matplotlib.pyplot as plt
import numpy as np

# Aula11 7c - Mola que se move periódicamente + Energia mecânica
# c)

v0 = 0
m = 1
k = 1
x0 = 4

dt = 0.001
t0 = 0
tf = 200
n = int((tf-t0)/dt)
g = 9.8

t = np.linspace(t0, tf, n)
vx = np.zeros(n) #or np.empty(n)
ax = np.zeros(n)
x = np.zeros(n)
v = np.zeros(n)
#equilibrio
e = np.zeros(n)
#energia mecanica
Em = np.zeros(n)


vx[0] = v0
x[0] = x0

# método de euler-cromer:
for i in range(n-1):
    ax[i] = -(k/m)*x[i]
    vx[i+1] = vx[i] + ax[i]*dt
    x[i+1] = x[i] + vx[i+1]*dt
    Em[i] = (0.5*m*(vx[i]**2)) + (0.5*k*(x[i]**2))
    
#definir o ultimo ponto
Em[n - 1] = (0.5*m*(vx[n - 1]**2)) + (0.5*k*(x[n - 1]**2))

#Amplitude/Periodo
Amax = []

tempos = []
periodos = []
       
for i in range(n-1):
    if (x[i-1] < x[i] > x[i+1] and i > 0):
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

print("O valor aproximado do período é: {:.4f}".format(T), "s")

    
plt.plot(t, x)
plt.xlabel("t /(s))")
plt.ylabel("x /(m)")
plt.grid()

plt.plot(t, e, "-r", label = "Equilíbrio")
plt.show() #dá "break" dos gráficos anteriores e mostra os que são escritos a seguir

plt.plot(t, Em, "-y")
plt.xlabel("t /(s))")
plt.ylabel("Em /(J)")
#definir limite de y
plt.ylim(5, 9)
plt.grid()

print()
print("TIME VARIABLES:")
print("---------------------------------")
print("t0 = {:0.3f} s".format(t0))
print("tF = {:0.3f} s".format(tf))
print("dT = {:0.3f} s".format(dt))
print("=================================")
print("VELOCITIES:")
print("Initial:")
print("v0 = {:0.4f} m/s".format(v0))
print("=================================")
print("POSITIONS:")
print("Initial:")
print("x0 = {:0.4f} m".format(x[0]))
print("---------------------------------")
print("=================================")
print("WAVE RELATED:")
print("A = {:0.4f} m".format(A))
print("T = {:0.4f} s".format(T))
print("---------------------------------")