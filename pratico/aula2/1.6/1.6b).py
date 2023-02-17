import numpy as np
import matplotlib.pyplot as plt

T = np.array([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
D = np.array([0.00,0.735,1.363,1.739,2.805,3.814,4.458,4.955,5.666,6.329])

# plt.scatter(T,D)
# plt.xlabel("T (min)")
# plt.ylabel("D (km)")

# b)
x = T
y = D

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