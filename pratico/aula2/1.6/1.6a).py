import numpy as np
import matplotlib.pyplot as plt

D = np.array([0.00,0.735,1.363,1.739,2.805,3.814,4.458,4.955,5.666,6.329])
# T = np.array([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
# ou
npontos = len(D)
print(npontos)
T = np.arange(0,10)
print(T)


# a)
plt.scatter(T,D)
plt.xlabel("T /(min)")
plt.ylabel("D /(km)")