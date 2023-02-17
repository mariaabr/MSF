import numpy as np
import matplotlib.pyplot as plt


T = np.array([200.0, 300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0, 1100.0])
E = np.array([0.6950, 4.363, 15.53, 38.74, 75.08, 125.2, 257.9, 344.1, 557.4, 690.7])


# b)

x = np.log(T)
print(x)
y = np.log(E)
print(y)

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

print('m = ',m)
print('b = ',b)
print('m*x + b = ',m,'*x +',b)
print('r2 = ',r2)

#  = math.log(b, base) + m*math.log(x, base)

plt.scatter(x,y)
plt.xlabel("T /(K)")
plt.ylabel("E /(J)")

x_g = np.arange(5.0,8,0.25)
l_g = m*x_g + b
plt.plot(x_g,l_g,"-")