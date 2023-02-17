import matplotlib.pyplot as plt
import numpy as np
import sympy as sym

t = sym.Symbol('t')
v = sym.Symbol('v')
a = sym.Symbol('a')
vT = sym.Symbol('vT')
g = sym.Symbol('g')
D = sym.Symbol('D')


# c)
D = sym.Derivative(vT*sym.sinh(g*t/vT)/sym.cosh(g*t/vT),t,evaluate=True)
print(D)
d = sym.simplify(D)
print(d)

vT = 6.80
g = 9.81
# gn = -9.81
tp = np.linspace(0,3,20)
a = g/np.cosh(g*tp/vT)**2
# an = g/np.cosh(gn*tp/vT)**2

plt.plot(tp, a, label = "a(t) do volante")
# plt.plot(tp, an, label = "a(t) do volante com g negativo")
plt.xlabel("t (s)")
plt.ylabel("a (m/s²)")
plt.title("Gráfico do volante :))")
plt.legend()