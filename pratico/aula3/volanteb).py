import matplotlib.pyplot as plt
import numpy as np
import sympy as sym



t = sym.Symbol('t')
v = sym.Symbol('v')
vT = sym.Symbol('vT')
g = sym.Symbol('g')
D = sym.Symbol('D')

# b)
D = sym.Derivative((vT**2)/g*sym.log(sym.cosh((g*t)/vT)),t,evaluate=True)
print(D)
d = sym.simplify(D)
print(d) 

vT = 6.80
g = 9.81
gn = -9.81
tp = np.linspace(0,4,20)
v = vT*np.tanh(g*tp/vT)
vn = vT*np.tanh(gn*tp/vT)

plt.plot(tp, v, label = "v(t) do volante")
plt.plot(tp, vn, label = "v(t) do volante com g negativo")
plt.xlabel("t (s)")
plt.ylabel("v (m/s)")
plt.title("Gráfico do volante :))")
plt.legend()
