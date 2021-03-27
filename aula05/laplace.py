
from math import e, sqrt
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
from  sympy import  Symbol
from sympy.abc import s, t, x, y,z
sym.init_printing()
def main():
    print(100*'#')

    print('# ')
    print(100*'#')
    print('\n')
    return valores()


def valores():
    f_zero,c,m, k, t = constantes()
    alpha = calculoAlfa(c,m)
    omega = calculoW(alpha, k, m)
    y_t = inversaLaplace(f_zero,k,m,alpha, t, omega)
    return imprimir( alpha, omega, y_t)

def constantes():
    c = 0.1
    m = 100.0
    k = 0.001
    t = 0
    f_zero = 1
    return f_zero,c,m, k, t

def calculoAlfa(c,m):
    return -c/2*m

def calculoW(alpha, k, m):
    return sqrt(alpha**2 - (k/m))

def inversaLaplace(f_zero, k, m, alfa, t, omega):
    return (f_zero / k * m) * ( 1 + (e**(alfa*omega)) * (1-omega / 2* omega * e**(omega*t) - (1+omega)/2*omega * e**-omega))

def imprimir(alpha,omega, y_t):
    print('Alfa: {}, Omega: {}, Y(t): {}'.format(alpha, omega, y_t))

if __name__ == '__main__':
    main()