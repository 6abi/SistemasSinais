import matplotlib.pyplot as plt
from math import cos, e, pi

#converte o ângulç
def converteAngulo(alfa):
    return (alfa * (pi / 180))

#tamanho do passo e tempo em segundos
def step():
    tempo = []
    for i in range(21):
        tempo.append(i * (1 / 10))
    return tempo

#resultado do sinusoide - x(t)
def sinusoide(a,tempo, b, omega, alfa):
    xt =[]
    for t in tempo:
        x = a * e**(-t*b) * cos(omega*t - alfa)
        xt.append(x)

    print('valores de x(t) variando de 0 até 2s com step 0.1')
    (print('x(t): {}'.format(xt)))
    return xt

#resultado da exponencial - e(t)
def expo(tempo, b):
    et = []
    for t in tempo:
        et.append(e**(-t*b))
    return et

#resultado da oscilação - A cos(w0t)
def ocilacao(a, tempo, omega):
    ot = []
    for t in tempo:
        ot.append(a * cos(omega*t))
    return ot

#gráfico genérico
def grafico(xt,et, ot, tempo, titulo):
    plt.ioff()
    print("\nCriando gráfico...")
    fig = plt.figure(figsize=(14, 12))
    plt.title(titulo)
    plt.grid(True)
    plt.xlabel('t(s)')
    plt.ylabel('(X(t))')
    plt.plot(tempo, xt, label = 'X(t)')
    plt.plot(tempo, et, label='e(t)')
    plt.plot(tempo, ot, label='A cos(w0t)')
    plt.legend()
    fig.savefig(titulo + ".png")
    print("Grafico criado, arquivo: "+ titulo + ".png")
    print("--Finished the program!--")

#grafico para a função A
def graficoA(xt, et, ot, tempo):
    return grafico(xt, et, ot, tempo, 'Gráfico A')

#grafico para a função B
def graficoB(xt, et, ot, tempo):
    return grafico(xt, et, ot, tempo, 'Gráfico B')

#grafico para a função C
def graficoC(xt, et, ot, tempo):
    return grafico(xt, et, ot, tempo, 'Gráfico C')

#grafico para a função D
def graficoD(xt, et, ot, tempo):
    return grafico(xt, et, ot, tempo, 'Gráfico D')

#grafico para a função E
def graficoE(xt, et, ot, tempo):
    return grafico(xt, et, ot, tempo, 'Gráfico E')

#Passagem dos valores de x(t), e(t), o(t) e passagem dos valores para o gráfico
if __name__ == '__main__':
    tempo = step()
    graficoA(sinusoide(3, tempo, 1, 9, converteAngulo(30)), expo(tempo, 1), ocilacao(3, tempo, 9), tempo)
    graficoB(sinusoide(3,tempo, 1, 9, (converteAngulo(30)* -1)), expo(tempo, 1), ocilacao(3, tempo, 9),tempo)
    graficoC(sinusoide(1, tempo, 0.1, 4, converteAngulo(45)), expo(tempo, 0.1), ocilacao(1, tempo, 4),tempo)
    graficoD(sinusoide(10, tempo, 6, 4, converteAngulo(45)), expo(tempo, 6), ocilacao(10, tempo, 4),tempo)
    graficoE(sinusoide(5, tempo, 1, 1, converteAngulo(0)), expo(tempo, 1), ocilacao(5, tempo, 1),tempo)


