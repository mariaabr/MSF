import numpy as np
import matplotlib.pyplot as plt

L = np.array([222.0,207.5,194.0,171.5,153.0,133.0,113.0,92.0])
X = np.array([2.3,2.2,2.0,1.8,1.6,1.4,1.2,1.0])

# plt.scatter(L,X)
# plt.xlabel("L (cm)")
# plt.ylabel("X (cm)")

x = L
y = X

xy = x*y
xx = x*x
yy = y*y

sxy = xy.sum()
sx = x.sum()
sy = y.sum()
sxx = xx.sum()
syy = yy.sum()

# print(" sxy: ", sxy)
# print(" sx: ", sx)
# print(" sy: ", sy)
# print(" sxx: ", sxx)
# print(" syy: ", syy)

# c)
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