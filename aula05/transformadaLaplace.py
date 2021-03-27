
from math import e, sqrt
import matplotlib.pyplot as plt
import numpy as np
import sympy
from  sympy import  Symbol
from sympy.abc import s, t, x, y,z
sympy.init_printing()
def main():
    print(100*'#')

    print('# ')
    print(100*'#')
    print('\n')


a = sympy.symbols('a', real=True, positive=True)
f = sympy.exp(-a*t)
sympy.integrate(f*sympy.exp(-s*t), (t, 0, sympy.oo))
F = sympy.laplace_transform(f, t, s, noconds=True)


def L(f):
    return sympy.laplace_transform(f, t, s, noconds=True)

def invL(F):
    return sympy.inverse_laplace_transform(F, s, t)

sympy.Heaviside(t)

sympy.plot(sympy.Heaviside(t))

invL(F).subs({a: 2})

p = sympy.plot(f.subs({a: 2}), invL(F).subs({a: 2}),
               xlim=(-1, 4), ylim=(0, 3), show=False)
p[1].line_color = 'red'
p.show()

omega = sympy.Symbol('omega', real=True)
exp = sympy.exp
sin = sympy.sin
cos = sympy.cos
functions = [1,
         t,
         exp(-a*t),
         t*exp(-a*t),
         t**2*exp(-a*t),
         sin(omega*t),
         cos(omega*t),
         1 - exp(-a*t),
         exp(-a*t)*sin(omega*t),
         exp(-a*t)*cos(omega*t),
         ]
print(functions)

Fs = [L(f) for f in functions]
print(Fs)

from pandas import DataFrame

def makelatex(args):
    return ["$${}$$".format(sympy.latex(a)) for a in args]

data = DataFrame(list(zip(makelatex(functions), makelatex(Fs))))
print(data)
