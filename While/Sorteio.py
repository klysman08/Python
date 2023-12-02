#58 sorteio
from random import randint
i = 0
u = int(randint(0, 10))
contador = 0
while (i != u):
    i = int(input('Escolha um numero de 0 a 10: '))
    contador += 1

print('Acertou!')
print(f'Você chutou {contador} vezes até acertar!')