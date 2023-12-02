contador = 0
from random import randint
while True:
    c = randint(0,10)
    n = int(input('1 para Par ou 2 para Impar: '))
    e = int(input('Escolha seu número: '))

    if n == 1 and ((e + c) % 2 == 0):
        print('Deu par!')
        print(f'Você escolheu {e} e o Pc escolheu {c}')
        print('Você ganhou!')
    elif n == 1 or n == 2 and (e + c) % 2 != 1:
        print('Você perdeu!')
        break

    elif n == 2:
        print('Deu impar')
        print(f'Você escolheu {e} e o Pc escolheu {c}')
        print('Você ganhou!')
    contador += 1

print(f'Numero de tentativas: {contador}')