import numpy as np
import matplotlib.pyplot as plt

M = np.array([0.15,0.20,0.16,0.11,0.25,0.32,0.40,0.45,0.50,0.55])
T2 = (np.array([1.21,1.40,1.26,1.05,1.60,1.78,2.00,2.11,2.22,2.33]))**2

R = np.arange(0,5)

# c)
x = M
y = T2

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
print('b +/-db= ',b ,"+/-",db)
print('r2= ',r2)

# sim, é um bom ajuste uma vez que o valor de r² é aproximadamente 1

# d)
K = 4*((np.pi)**2)*(1/m)
print()
print("A constante elástica é igual a: ", K)