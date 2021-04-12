
from math import e, sqrt
import numpy as np

# define f(t,u)
def f(t, u):
    return t*e**-t*u


# tamanho e num. de passos
h = 0.2
N = 6

# cria vetor t e u
t = np.empty(N)
u = np.copy(t)

# C.I.
t[0] = 0
u[0] = 1

# iteracoes
for i in np.arange(N - 1):
    t[i + 1] = t[i] + h
    u[i + 1] = u[i] + h * f(t[i], u[i])

# imprime
for i, tt in enumerate(t):
    print("%1.1f %1.4f" % (t[i], u[i]))