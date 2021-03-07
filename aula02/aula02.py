
#######################################################
#       (+∞)
##### E=∫ 〖|x(t)|〗^2  dt〗
#       (-∞)
######################################################
#               (T/2)
# P= lim〖1/T〗 ∫ 〖|x(t)|〗^2  dt〗
#    (T→∞)      (-T)/2)
######################################################


from sympy import *
from math import e, sqrt

init_printing(pretty_print=true)



def main():
    print(100*'#')

    print('EXERCICIO: Implemente um algoritmo em python para calcular a energia ou potência e valor\n '
          'rms utilizando o método da exaustão onde o usuário escolhe o tamanho do passo delta t para\n '
          'os sinais dados\n')
    print(100*'#')

    #chamada das funções para cálculo
    tamanhoPasso()


#delta
def tamanhoPasso():
    print(' Digite o tamanho do passo \n Sugestão: (0.001 ou 0.0001)')
    delta_t = input('delta t: ')

    return trataErro(delta_t)

#trata valor
def trataErro(delta_t):
    try:
        delta_t = float(delta_t)
    except ValueError:
        print('Digite um valor numérico!')
        return tamanhoPasso()
    if(delta_t < 0):
        print(' Para o tamanho do passo, por favor, digite valores positivos! ')
        return tamanhoPasso()
    #passa valores para calculo
    return energia(0,2,delta_t)


#mostra na tela os valores
def imprimir(energia,energia2, p, rms, intervalo):
    print(100 * '#')
    print('intervalo de integração da Energia: {}'.format(intervalo))
    print('Energia: {}  com integral exata '.format(energia))
    print('Energia: {} com método da exaustão '.format(energia2))
    print(100 * '#')
    print('intervalo de integração da Potência: {}'.format([-1,1]))
    print('Potência: {}  com integral exata '.format('1/3'))
    print('Potência: {} com método da exaustão '.format(p))
    print('Potência RMS: {} com método da exaustão '.format(rms))


#calcula energia com método da exaustão e integral exata
def energia(tempo_i, tempo_f, delta_t):
    t = Symbol('t')
    tempo = tempo_i
    energia = 0
    energia2 = 0

    while tempo < tempo_f:
        if((-1 <= tempo_i <= 0)):
            #integral exata
            energia = (Integral(abs(2**2) , (t, tempo_i, tempo_f)).doit())
            #por exaustão
            energia2 += abs(2**2) * delta_t

        elif(tempo_i >= 0 and tempo_f > 0):
            #integral exata
            energia = (Integral(abs(2*(e**(-t/2)))**2, (t, tempo_i, tempo_f)).doit())
            #por exaustão
            energia2 += abs(2*(e**(-tempo/2)))**2 * delta_t
        else:
            energia2 += 0
        tempo += delta_t

    imprimir(round(energia,4), round(energia2,4),potencia(delta_t, -1/2,1/2), rms(potencia(delta_t, -1/2,1/2)), [tempo_i,tempo_f])

#calcula potencia
def potencia(delta_t, tempo_i,tempo_f):
    t = Symbol('t')
    p = 0
    tempo = tempo_i
    while tempo < 1:
        p += abs(tempo)**2 * delta_t
        tempo += delta_t
    rms(p)
    return round(p,6)

#calcula rms
def rms(p):
    return round(sqrt(p), 4)


if __name__ == '__main__':
    main()



