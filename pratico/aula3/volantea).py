import matplotlib.pyplot as plt
import numpy as np

# a)
vT = 6.80
g = 9.81

t = np.linspace(0,4,20)

yt = (vT**2)/g*np.log(np.cosh((g*t)/vT))


plt.plot(t, yt, label = "y(t) do volante")
plt.xlabel("t /(s)")
plt.ylabel("x(m)")
plt.title("Gráfico do volante :))")
plt.legend()