# construir um algoritmo que calcule a convolução entre um sinal entrada x(t) e a resposta do sistema h(t)
# e mostre a resposta y(t). Para isso, utilize um método numérico para calcular integrais como o método
# dos trapézios, simpson, etc. Os sinais x(t) são do tipo sen(beta*t)  e as respostas h(t)
# são do tipo exp(-alfa*t). Sempre iniciando em t=0. Faça um teste integrando de 0 a t = 2 com alfa = -2
# e beta = 3. Mostra o resultado por meio de cálculo analítico e o resultdo obtido com o método numérico.
#       −∞
#y(t) = ∫ h(τ)x(t−τ)dτ
#       ∞
from math import sin, e
import matplotlib.pyplot as plt
import numpy as np

def main():
    print(100*'#')

    print('# construir um algoritmo que calcule a convolução entre um sinal entrada x(t) e a resposta do sistema h(t)\n '
          'e mostre a resposta y(t). Para isso, utilize um método numérico para calcular integrais como o método\n '
          'dos trapézios, simpson, etc. Os sinais x(t) são do tipo sen(beta*t)  e as respostas h(t)\n '
          'são do tipo exp(-alfa*t). Sempre iniciando em t=0. Faça um teste integrando de 0 a t = 2 com alfa = -2 \n'
          'e beta = 3. Mostra o resultado por meio de cálculo analítico e o resultdo obtido com o método numérico.\n\n'
          'Integral de Convolução\n'
          '       −∞\n'
          'y(t) = ∫ h(τ)x(t−τ)dτ\n'
          '       ∞\n'
          )
    print(100*'#')
    print('\n')

    #****passa os valores para calculo****
    # n passos, intervalo e valor de t
    n = 1000
    t_final = 2
    dt = float(t_final) / n
    tempo = [dt * i for i in range(n)]

    # valores para h(t) e x(t)
    h_t = hT(-2, tempo)
    x_t = xT(3, tempo)

    # Cálculo método Analítico
    analitico = convolucaoAnalitico(3, -2, tempo)

    # Cálculo método Trapézio
    trapezio = convolucaoTrapezio(x_t, h_t, dt)

    #gráfico
    grafico(analitico, trapezio, tempo, "Integral de Convolução")

#sinal de entrada x(t)
def xT(beta, tempo):
    y2 = []
    for t in tempo:
        x = sin(beta*t)
        y2.append(x)
    return y2


#resposta do impulso h(t)
def hT(alfa, tempo):
    y1 = []
    for t in tempo:
        x = e**(-alfa*t)
        y1.append(x)
    return y1


#calculo da integral de convolução - método do trapézio
def convolucaoTrapezio(x_t, h_t, dx = None):
    # tamanho do sinal
    P = len(h_t)
    z = []

    # calculo integral
    for j in range(P):
        t = 0
        t_min = max(0, j - (P - 1))
        t_max = min(P - 1, j)
        for i in range(t_min, t_max):
            t += (h_t[i] * x_t[j - i] + h_t[i + 1] * x_t[j - (i + 1)]) / 2
        z.append(t)
    z = np.array(z)
    if dx != None:
        z *= dx
    return z

#Cálculo método Analítico
def convolucaoAnalitico(beta, alfa, tempo):
    a = []
    for t in tempo:
        x = sin(beta * t) * -1 + e**(-alfa * t)
        a.append(x)
    return a


def grafico(analitico,trapezio, t, titulo):
    plt.ioff()
    print('Intevalo de integração: t[0,2]')
    print("\nCriando gráfico...")
    fig = plt.figure(figsize=(14, 12))
    plt.title(titulo)
    plt.grid(True)
    plt.xlabel('t(s)')
    plt.ylabel('Y(t)')
    plt.plot(t, analitico, label='Analítica')
    plt.plot(t, trapezio, 'o', label='Trapézio')
    plt.legend()
    fig.savefig(titulo + ".png")
    print("Grafico criado, arquivo: "+ titulo + ".png")
    print("--Finished the program!--")
    plt.show()

if __name__ == '__main__':
    main()
