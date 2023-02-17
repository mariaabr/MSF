import numpy as np
import matplotlib.pyplot as plt

t = np.array([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5])**1.948
s = np.array([0.121,0.997,2.55,6.09,9.31,15.8,17.1,25.5,26.5,38.8,41.9])

R = np.arange(0,50)

# c)

plt.scatter(t,s)
plt.xlabel("t /(s)")
plt.ylabel("s /(m)")

x = t
y = s

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

t = np.arange(0.0,100,1.0)
rl = m*t + b
plt.plot(t,rl,"r-")