import numpy as np
import matplotlib.pyplot as plt

M = np.log(np.array([0.15,0.20,0.16,0.11,0.25,0.32,0.40,0.45,0.50,0.55]))
T = np.log(np.array([1.21,1.40,1.26,1.05,1.60,1.78,2.00,2.11,2.22,2.33]))

R = np.arange(0,5)

# b)
plt.scatter(M,T)
plt.plot(M,T)
plt.xlabel("M /(kg)")
plt.ylabel("T /(s)")

# resposta da dependência: linear, quadrática ou exponencial
# neste caso, a dependência é çinear uma vez que se observa uma reta no gráfico

x = M
y = T

xy = x*y
xx = x*x
yy = y*y
  
sxy = xy.sum()
sx = x.sum()
sy = y.sum()
sxx = xx.sum()
syy = yy.sum()

npontos = x.size
n=npontos
rn=n*sxy-sx*sy
rd=(n*sxx-sx**2)*(n*syy-sy**2)
r2=rn**2/rd
r=np.sqrt(r2)
m=(n*sxy-sx*sy)/(n*sxx-sx**2)
dm=abs(m)*np.sqrt((1/r**2-1)/(n-2))
bn=sxx*sy-sx*sxy  
bd=n*sxx-sx**2
b=bn/bd
db=dm*np.sqrt(sxx/n)


print('m +/-dm= ',m ,"+/-", dm)
# print('b +/-db= ',b ,"+/-",db)
print('r2= ',r2)