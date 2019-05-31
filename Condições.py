
'''#from random import randint
#from time import sleep
#comp = randint(0,5)

#a = int(input('Escolha um numero: '))
#print('Pensando...')
#sleep(4)
#if a == comp :
#    print('Parabens, voce acertou')
#else:
#    print('Voce Errou')
#print('Ele pensou no {}'.format(comp))

#v = int(input('Qual a velocidade do carro: '))
#if  v >= 50:
#    print('Você foi multado')
#    m = v - 50
#    print('Você deve pagar uma multa no valor de {} reais'.format(m*7))
#else:
#    print('Tudo certo')

#n = int(input('Digite um número'))
#r = n % 2
#if r == 0:
#    print('O numero é par')
#else:
#    print('Numero impar')

d = float(input('Qual a distancia da sua viagem? '))
if  d <= 200:
    print('O valor da sua viagem ficou em {:.f} reais '.format(d*0.5))
else:
    print('O valor da sua viagem, como promoção, ficou {:.2f} reais '.format((d*0.45)))

a = int(input('Digite o priemiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > a:
    maior = a
if c > a and c > b:
    maior = c

print('O maior valor é {} e o menor valor é {} '.format(maior, menor))

n = [a,b,c]
print('O maior valor é {} e o menor valor é {} '.format(max(n),min(n)))

a = int(input('Qual o salario do funcionario? '))

if a <= 1250:
    print('O novo salário é {:.3f}'.format(a*1.15))
else:
    print('O novo salário é {:.3f}'.format(a*1.10))

a = int(input('Digite a primeira medida '))
b = int(input('Digite a segunda medida '))
c = int(input('Digite a terceira medida'))

if a < b+c and b < a+c and c < a+b:
    print('Parabens')
else:
    print('Impossível formar o triangulo')'''







