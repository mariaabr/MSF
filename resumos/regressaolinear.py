import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0,50) # vai de 0 a 50o gráfico

x = # ?
y = # ?
# definir os ?
# numa relação o que se pronuncia primeiro é o y (y/x)

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