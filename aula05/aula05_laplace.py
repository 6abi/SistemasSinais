# -*- coding: utf-8 -*-
"""Aula05_Laplace.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DihzLTKMtTpRk6An__ZoLN7D_HUVtQvP
"""

import matplotlib.pyplot as plt
import sympy
from  sympy import  Symbol
# from sympy.abc import s, t, c, m, k
from math import e, sqrt
sympy.init_printing()

#simbolos
t, s, a = sympy.symbols('t, s, a')
m = sympy.symbols('m', real=True, positive=True)
c = sympy.symbols('c', real=True, positive=True)
k = sympy.symbols('k', real=True, positive=True)
alfa = sympy.symbols('alfa', real=True, positive=True)
omega = sympy.symbols('omega')
f_zero = sympy.symbols('f_zero', real=True, positive=True)
y = sympy.Function('y')

##definição da expressão( EDO)
f = m * y(t).diff(t).diff(t) + c * y(t).diff(t) + k* y(t)
F = sympy.laplace_transform(f, t, s, noconds=True)

#transformada
def L(f):
    return sympy.laplace_transform(f, t, s, noconds=True)

#transformada inversa
def invL(F):
    return sympy.inverse_laplace_transform(F, s, t)

#função unitaria e expressão( EDO)
u = sympy.Function('u')
u = 1

#transformada Laplace separadas (EDO)
f,u

#valores para o calculo
Y = (L(f) - f_zero/s)
Y.subs({c: 2, f_zero: 3, k: 1, m: 1})

#transformação inversa (EDO)
invL(F)

#alfa
alfa = -c/2*m

#omega
omega = ((alfa**2) - (k/m))**(1/2)

#expressão transformada Laplace t0
Y =  sympy.Function('Y')
Y = f_zero*m / (k* (m * s**2 + c * s + k))
Y

#plotagem transformada

p = sympy.plot(Y.subs({m: 50, c: 4, k: 3, f_zero: 1}), Y.subs({m: 50, c: 4, k: 3, f_zero: 1}),
               xlim=(-0.001, 3), ylim=(0, 9), show=False)
p[1].line_color = 'red'

p.show()

#unit step function
sympy.Heaviside(t)
sympy.plot(sympy.Heaviside(t))

#inversa
invL(F).subs({m: 2, c: 3, k: 3, f_zero: 2})

#plotagem transformada inversa
p = sympy.plot(invL(Y).subs({m: 50, c: 3, k: 3, f_zero: 2}), invL(Y).subs({m: 50, c: 3, k: 3, f_zero: 2}),
               xlim=(0, 8), ylim=(0, 9), show=False)
p[1].line_color = 'red'
p.show()

#funções tabela
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
functions

#tabela
Fs = [L(f) for f in functions]
Fs

from pandas import DataFrame
def makelatex(args):
    return ["$${}$$".format(sympy.latex(a)) for a in args]

DataFrame(list(zip(makelatex(functions), makelatex(Fs))))