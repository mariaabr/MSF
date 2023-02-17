import numpy as np
import matplotlib.pyplot as plt

L = np.array([222.0,207.5,194.0,171.5,153.0,133.0,113.0,92.0])
X = np.array([2.3,2.2,2.0,1.8,1.6,1.4,1.2,1.0])


def regrlinear(x,y):    
    x = L
    y = X
    
    plt.scatter(x,y)
    plt.xlabel("L (cm)")
    plt.ylabel("X (cm)")
    
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
    
    x_g = np.arange(80,240,10)
    l_g = m*x_g + b
    plt.plot(x_g,l_g,"-")
    
    return m,b


#f)

print(regrlinear(L,X))
X = np.array([2.3,2.2,2.0,1.8,2.5,1.4,1.2,1.0])
print(regrlinear(L,X))
