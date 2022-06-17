
def calcula_velocidade(velocidade, aceleracao, tempo):
    
    """ velocidade = int(input("Digite o valor da velocidade:"))
    aceleracao = int(input("Digite o valor da aceleração:"))
    tempo = int(input("Digite o valor do tempo:")) """


    velocidade_final = velocidade + (aceleracao * tempo)
    distancia_percorrida = velocidade * tempo + (aceleracao * (tempo**2)) / 2

    print("Velocidade final:", velocidade_final.__format__('0.2f'))
    print("Distancia percorrida:", distancia_percorrida.__format__('0.2f'))

    return velocidade_final, distancia_percorrida

calcula_velocidade(10, 2, 5)


def func(x):
    return x + 1