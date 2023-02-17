import matplotlib.pyplot as plt
import numpy as np

# Aula12 1 - Mola que se move periódicamente + Amplitude e período num oscilador harmónico forçado no regime estacionário ( que precisa de ser definido)
# f)

def abfourier(tp,xp,it0,it1,nf):
#
# cálculo dos coeficientes de Fourier a_nf e b_nf
#       a_nf = 2/T integral ( xp cos( nf w) ) dt   entre tp(it0) e tp(it1)
#       b_nf = 2/T integral ( xp sin( nf w) ) dt   entre tp(it0) e tp(it1)    
# integracao numerica pela aproximação trapezoidal
# input: matrizes tempo tp   (abcissas)
#                 posição xp (ordenadas) 
#       indices inicial it0
#               final   it1  (ao fim de um período)   
#       nf índice de Fourier
# output: af_bf e bf_nf  
# 
    dt=tp[1]-tp[0]
    per=tp[it1]-tp[it0]
    ome=2*np.pi/per

    s1=xp[it0]*np.cos(nf*ome*tp[it0])
    s2=xp[it1]*np.cos(nf*ome*tp[it1])
    st=xp[it0+1:it1]*np.cos(nf*ome*tp[it0+1:it1])
    soma=np.sum(st)
    
    q1=xp[it0]*np.sin(nf*ome*tp[it0])
    q2=xp[it1]*np.sin(nf*ome*tp[it1])
    qt=xp[it0+1:it1]*np.sin(nf*ome*tp[it0+1:it1])
    somq=np.sum(qt)
    
    intega=((s1+s2)/2+soma)*dt
    af=2/per*intega
    integq=((q1+q2)/2+somq)*dt
    bf=2/per*integq
    return af,bf

v0 = 0
m = 1
k = 1
x0 = 4
b = 0.05
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

#array até 1000 frequências necessário para os coeficientes de fourier
ind = np.transpose([0 for i in range(1000)])

af0 = np.zeros(15)
bf0 = np.zeros(15)

vx[0] = v0
x[0] = x0

# método de euler-cromer:
for i in range(n-1):
    ax[i] = -(k/m)*x[i] - (b/m)*vx[i] + (F0/m)*np.cos(w*t[i])
    vx[i+1] = vx[i] + ax[i]*dt
    x[i+1] = x[i] + vx[i+1]*dt
    

#Amplitude/Periodo
Amax = []
tempos = []
periodos = []
countMax = 0

for i in range(n-1):
    if (x[i-1] < x[i] > x[i+1] and t[i] > 200):
        Amax.append(x[i])
        tempos.append(t[i])
        countMax += 1
        ind[countMax] = int(i)
        
        
for i in range(1, len(tempos)-1):
    temp = tempos[i+1] - tempos[i]
    periodos.append(temp)

    
A = sum(Amax)/(len(Amax))       
T = sum(periodos)/(len(periodos))

# for i in range(n):
#     if t[i] > 200 and x[i - 1] > x[i] and x[i + 1] > x[i]:
#         countMax += 1
#         ind[countMax] = int(i)

# #PRINTS
        
# print(Amax)
# print(periodos)

# print("O valor aproximado da amplitude é: {:.4f}".format(A), "m")

# print("O valor aproximado da amplitude é: {:.4f}".format(T), "s")

t0 = ind[countMax - 1]
t1 = ind[countMax]
for i in range(15):
    af, bf = abfourier(t, x, t0, t1, i)
    af0[i] = af
    bf0[i] = bf

ii = np.linspace(0,14,15)  
plt.plot(t, x)
plt.xlabel(" n ")
plt.ylabel("| an |")
plt.bar(ii, np.abs(af0))
plt.grid()

ii = np.linspace(0,14,15)  
plt.plot(t, x)
plt.xlabel(" n ")
plt.ylabel("| bn |")
plt.bar(ii, np.abs(bf0))
plt.grid()