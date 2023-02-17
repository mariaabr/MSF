import numpy as np
import matplotlib.pyplot as plt

L = np.array([222.0,207.5,194.0,171.5,153.0,133.0,113.0,92.0])
X = np.array([2.3,2.2,2.0,1.8,1.6,1.4,1.2,1.0])

# plt.scatter(L,X)
# plt.xlabel("L (cm)")
# plt.ylabel("X (cm)")

# b)
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

print(" sxy: ", sxy)
print(" sx: ", sx)
print(" sy: ", sy)
print(" sxx: ", sxx)
print(" syy: ", syy)