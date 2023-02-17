import numpy as np
import matplotlib.pyplot as plt

# normal
plt.scatter(t,s)
plt.xlabel("t /(s)")
plt.ylabel("s /(m)")


# reta regressão linear
t = np.arange(0.0,14.5,0.50)
rl = m*t + b
plt.plot(t,rl,"r-")

