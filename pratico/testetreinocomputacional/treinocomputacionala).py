import numpy as np
import matplotlib.pyplot as plt

M = np.array([0.15,0.20,0.16,0.11,0.25,0.32,0.40,0.45,0.50,0.55])
T = np.array([1.21,1.40,1.26,1.05,1.60,1.78,2.00,2.11,2.22,2.33])

R = np.arange(0,5)

# a)
plt.scatter(M,T)
plt.xlabel("M /(kg)")
plt.ylabel("T /(s)")


# a relação entre T e M não é linear porque os pontos não formam uma reta