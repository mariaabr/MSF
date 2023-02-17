import numpy as np
import matplotlib.pyplot as plt
import math

dt=0.001
ti= 0
tf=200.00
n=int((tf-ti)/dt)

t=np.linspace(ti,tf,n)

potencia=0.48*735.49875
mu=0.001
Cres=0.9
A=0.50
densidade=1.225
massa=72
g=9.8
angulo = 5
v0=0.5
fAtrito=-mu*massa*g*math.cos(np.radians(5))
#fAtrito=-mu*massa*g #segundo sugetão do Torres. Ver apontamentos

#Aqui uso n+1 por ser mais facil interpretar a formula da integração --> nós usamos sempre n
v=np.empty(n)
vx=np.empty(n)
x=np.empty(n)
ax=np.empty(n)
aresx=np.empty(n)
ftro=np.empty(n)

vx[0]=v0
x[0]=0
tolerancia=0.00000001
pesoX=-massa*g*math.sin(np.radians(5))

for i in range(n-1):
    v[i]=np.sqrt(vx[i]**2)
    aresx[i]=-Cres/(2*massa)*A*densidade*v[i]*vx[i]
    ftro[i]=potencia/(massa*v[i])
    
    ax[i]=fAtrito/massa+aresx[i]+ftro[i]+pesoX/massa
    vx[i+1]=vx[i]+ax[i]*dt
    x[i+1]=x[i]+vx[i]*dt
    
    #velocidade terminal: considerar um valor muito pequeno a partir do qual e igual
    if (x[i+1]>2000):
        print ("temp x=2km = ",t[i],"s")
        break

v[i+1]=np.sqrt(vx[i+1]**2)


plt.plot(t,v, color = "darkblue")
#plt.plot(t,energia,label='W Res')
plt.ylabel('V (m/s)')
plt.xlabel( 't (s)' )
plt.grid()
plt.title("Tempo para percorrer 2 km com 5º de inclinação")