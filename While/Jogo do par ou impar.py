contador = 0
from random import randint
while True:
    c = randint(0,10)
    n = int(input('1 para Par ou 2 para Impar: '))
    e = int(input('Escolha seu número: '))

    if ( n == 1):
        if ( (e+c) % 2 == 0 ):
            print('Deu par!')
            print(f'Você escolheu {e} e o Pc escolheu {c}')
            print('Você ganhou!')
        else:
            print('Você perdeu!')
            break

    if ( n == 2):
        if ((e+c) % 2 == 1):
            print('Deu impar')
            print(f'Você escolheu {e} e o Pc escolheu {c}')
            print('Você ganhou!')
        else:
            print('Você perdeu!')
            break

    contador += 1

print(f'Numero de tentativas: {contador}')