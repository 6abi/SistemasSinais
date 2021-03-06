# -*- coding: utf-8 -*-
"""Aula12_serie_fourier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e_oJvWViik1EvcQHg3Zjri-tELzZaBls

# Bárbara Cardoso

# Ado Serie de Fourier. O usurário poderá entrar com o valores da amplitude A e n.

# Para executar todas as células: Ambiente de execução --> Executar tudo
## Na secção "Input do usuário" Digite os valores para n e A

## Import de bibliotecas
"""

import matplotlib.pyplot as plt
from numpy import sin, cos
import numpy as np

"""## Input do usuário"""

n = int(input(' Insira o valor para n(maior do que 1!): '))
A = float(input('Insira o valor da amplitude A: '))

"""## intervalo de tempo

"""

t = np.linspace(0, 10, 100) # 500 números, de 0 a 10 -> 1 kHz de amostragem

"""## Funções para cálculo da Série

"""

def main():
  y = []
  for i in range(len(t)):
      x = np.array(sF(n, A, t[i]))
      y.append(x)
  return grafico(t,y)

def f(n, A):
    return (A* 0.5) * ( np.sin(cos(n) / n) + (np.sin(n) / (n**2)) )

def g(n, A):
    return 0.5 * ( -A* ( (-np.cos(n)/n) + (np.sin(n)/(n**2)) + (3*np.cos(3*n)/n) - (np.sin(3*n)/(n**2))) + (2*A)* ((-1/n) * np.cos(n) + (1/(3*n)) * np.cos(3*n)))

def h(n, A):
    return 0.5 * ( A*( -(3*np.cos(3*n) / n) + (np.sin(3*n) / (n**2)) + (4*np.cos(4*n) / n) - (np.sin(4*n) / (n**2)) ) - 4*A*( -( 1/(3*n) * np.cos(3*n)) + (1/(4*n) *np.cos(4*n)) ) )

"""## Cálculo da Serie """

def sF(N, A, t):
    sum = np.zeros(np.size(t))
    for i in np.arange(1, N+1):
        if t % 4 == 1:
            sum += f(N, A) * np.sin(N*t)
        elif t % 4 <= 3:
            sum += g(N, A) * np.sin(N*t)
        else:
            sum += h(N, A) * np.sin(N*t)
    return sum

"""## Plotagem do gráfico"""

def grafico(t,y):
    plt.ioff()
    fig = plt.figure(figsize=(15, 8))
    plt.title("Série Fourier - ADO aula 12")
    plt.grid(True)
    plt.xlabel('t(s)')
    plt.ylabel('Amplitude')
    plt.plot(t,y)
    plt.show()

if __name__ == '__main__':
  main()