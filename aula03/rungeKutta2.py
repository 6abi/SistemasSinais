import matplotlib.pyplot as plt
import math


r = int(input('Valor de R(ohms): '))
l = float(input('Valor de L(Henrys): '))
c = float(input('Valor de C(Farads): '))

def main():
    print(100*'#')
    print('Resolva a equação do sistema elétrico mostrada anteriormente. Faça a escrita manual. \n'
          'Em seguida, utilize o método de Runge-Kutta de ordem 4 e resolva o mesmo sistema utilizando\n'
          'uma linguagem de programação. Mostre os gráficos de x(t) e y(t) de modo que o usuário\n'
          'possa inserir as entradas R (ohms), L (Henrys) e C (Farads).')
    print(100*'#')


#primeira derivada de v
def dvDt(t, v, z):
    return ( (-v)/(r*c) + z/c)

#segunda derivada de v
def dvDt2(t, v, z):
    return ( (-v)/l*c - z/(r*c) + v_s/(l*c))

def grafico(xt,yt, t, titulo):
    plt.ioff()
    print("\nCriando gráfico...")
    fig = plt.figure(figsize=(14, 12))
    plt.title(titulo)
    plt.grid(True)
    plt.xlabel('t(s)')
    plt.ylabel('(X(t))')
    plt.plot(t, xt, label = 'X(t)')
    plt.plot(t, yt, label='Y(t)')

    plt.legend()
    fig.savefig(titulo + ".png")
    print("Grafico criado, arquivo: "+ titulo + ".png")
    print("--Finished the program!--")

#runge kutta ordem 4
def RK4(fx, gx, x0, y0, t0, h, n):

    x = []
    y = []
    t = []
    i = 1
    t.append(t0)
    x.append(x0)
    y.append(y0)
    x[0] = x0

    for i in range(1, n):
        t.append((t[i-1] + h))
        k1 = h*fx(t[i - 1], x[i - 1], y[i - 1])
        k21 = h * fx(t[i - 1], x[i - 1], y[i - 1])

        k2 = h*fx(t[i - 1] + h / 2, x[i - 1] + k1 / 2, y[i - 1] + k21 / 2)
        k22 = h*gx(t[i - 1] + h / 2, x[i - 1] + k1 / 2, y[i - 1] + k21 / 2)

        k3 = h*fx(t[i - 1] + h / 2, x[i - 1] + k2/2, y[i - 1] + k22 / 2)
        k23 = h*gx(t[i - 1] + h / 2, x[i - 1] + k2/2, y[i - 1] + k22 / 2)

        k4 = h*fx(t[i - 1] + h/2, x[i - 1] + k3, y[i - 1] + k23)
        k24 = h*gx(t[i - 1] + h/2, x[i - 1] + k3, y[i - 1] + k23)

        x.append(x[i - 1] + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4))
        y.append(y[i - 1] + (1/ 6) * (k21 + 2 * k22 + 2 * k23 + k24))
    grafico(x, y, t, 'Runge Kutta Ordem 4')
    return x,y,t


x0 = 0
y0 = 0
t0 = 0
h = 0.0001
n = 1000
v_s = 120

x,y, t = RK4(dvDt,dvDt2, x0,y0,t0,h,n)

if __name__ == '__main__':
    main()


