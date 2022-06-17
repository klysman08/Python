def dobro_int(x):
    return x * 2


def sinal(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0
    
def consumo(distancia, quantidade_litros):
    if distancia / quantidade_litros < 8: 
        return print('Venda o carro')
    elif distancia / quantidade_litros <= 12:
        return print('Econômico')
    else:
        return print('Super econômico')
    
    
def total_segundos(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos

def paridade(x):
    if x % 2 == 0:
        return True
    else:
        return False
    
import math
    
def volume_esfera(raio):
    return 4/3 * math.pi * (raio ** 3)

def hipotenusa(cateto1, cateto2):
    return math.sqrt(cateto1 ** 2 + cateto2 ** 2)

def peso_ideal(altura, sexo):
    if sexo == 'm':
        return 72.7 * altura - 58
    else:
        return 62.1 * altura - 44.7
    
def soma_digitos(x):
    soma = 0
    while x > 0:
        soma += x % 10
        x //= 10
    return soma


def estacionamento(horas_chegada, minutos_chegada, hora_saida, minuto_saida):

    minutos1 = horas_chegada* 60 + minutos_chegada
    minutos2= horas_saida * 60 + minutos_saida
    minutos_totais = minutos2 - minutos1
    
    horas_totais = minutos_totais // 60
    
    if horas_totais <=2:
        return horas_totais * 1.00
    elif horas_totais >= 3 and horas_totais <= 4:
        return horas_totais * 1.40
    else:
        return horas_totais * 2.00