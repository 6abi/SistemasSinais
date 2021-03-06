# -*- coding: utf-8 -*-
"""sistemas-e-sinais-p2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XhI7NxCfrqrrMeoIX0sFJLu5IghjeTm3

# Bárbara cardoso

# Para executar todas as células: Ambiente de execução --> Executar tudo

# O exerciocio e o valor dx/dy calculado

**Escreva um programa em python que faça o gráfico da função y=y(x) da letra b) e da leta c) abaixo e das respectivas derivadas dessa funções, dy/dx.**
"""

import matplotlib.pyplot as plt
import sympy as sym
from  sympy import  symbols
from math import e as E, sqrt
from sympy.plotting import plot3d, plot_implicit, plot
sym.init_printing()

"""## drive para salvar os gráficos"""

from google.colab import drive
drive.mount('/content/drive')

"""## Declaração variaveis e funções"""

x,y, e, dy, dx = symbols("x y e dy dx")
f, g  = symbols("f g ", cls=Function)
intervalo = 10

"""## ITem B

### Com a biblioteca Sympy

#### Equação
"""

#equação
f = y + e**y - x -2
f_b = sym.Eq(y + E**y - x, 2)
f_b

f

"""#### Dy/Dx"""

b = sym.idiff(f,y,x)
dy_dxb = sym.Eq(dy/dx,b)
dy_dxb

"""#### Gráficos

##### Equação
"""

b_func = y + E**y - x -2
p1 = plot3d(b_func,(x, -8,8), (y, -8, 8), 
            #adaptive=False, nb_of_points_x = intervalo, nb_of_points_y =intervalo,
            title = "Gráfico da equação b: {}".format(f), 
            size = (8,6), xlabel='x', ylabel='y')
p1

"""#### Dy/Dx

###### Dy/Dx com a biblioteca sympy
"""

p2 = plot(1 / (E**y +1),(x, -6,6), (y, -6, 6),
            adaptive=False, nb_of_points = 100,
            title = "Gráfico da equação c: {}".format(b_func), 
            size = (8,6), xlabel='x', ylabel='y')

"""###### implicit"""

p = plot_implicit(f_b, (x, -10,10), (y, -10, 10),
                   adaptive = False, points = 1000, size = (8,6),
                   title = "Gráfico Dx/Dy = {}".format(b_func))

p = plot3d(1 / (E**y +1),(x, -6,6), (y, -6, 6),
            # adaptive=False, nb_of_points_x = 10, nb_of_points_y = 10,
            title = "Gráfico Dy/Dx da questão c",
            size = (8,6), xlabel='x', ylabel='y')

"""## ITem C

#### Equação
"""

#equação
g = (x**2 + y**2)**(3/2) - 10*x*y
f_c =  sym.Eq((x**2 + y**2)**(3/2), 10*x*y)
f_c

c

"""#### Dy/Dx"""

dy_c = sym.idiff(c,y,x)
dy_dxc = sym.Eq(dy/dx,dy_c)
dy_dxc

"""#### Gráficos

##### Equação
"""

p3 = plot3d(g,(x, -8,8), (y, -8, 8), 
            #adaptive=False, nb_of_points_x = intervalo, nb_of_points_y =intervalo,
            title = "Gráfico da equação c: {}".format(g), 
            size = (8,6), xlabel='x', ylabel='y')

"""##### Dx/Dy

###### Dy/Dx com a biblioteca sympy
"""

p4 = plot_implicit(f_c, (x, -5,5), (y, -5, 5),
                   adaptive=False, nb_of_points=300, 
                   title = "Gráfico Dy/Dx da questão c,")

p5 = plot3d(dy_c,(x, -6,6), (y, -6, 6),
            #adaptive=False, nb_of_points_x = intervalo, nb_of_points_y =intervalo,
            title = "Gráfico Dy/Dx da questão c",
            size = (8,6), xlabel='x', ylabel='y')
p5

p1.save('/content/drive/MyDrive/1.P2/p1.png')
p2.save('/content/drive/MyDrive/1.P2/p2.png')
p3.save('/content/drive/MyDrive/1.P2/p3.png')
p4.save('/content/drive/MyDrive/1.P2/p4.png')
p5.save('/content/drive/MyDrive/1.P2/p5.png')