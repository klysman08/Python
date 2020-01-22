from random import randint
from time import sleep
comp = randint(0,5)

a = int(input('Escolha um numero: '))
print('Pensando...')
sleep(4)
if a == comp :
    print('Parabens, voce acertou')
else:
    print('Voce Errou')
print('Ele pensou no {}'.format(comp))