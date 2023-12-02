from random import randint
from time import sleep


n = int(input('Quantos jogos devem ser gerados? '))
lista = []
for _ in range(0, n):
    lista.extend(randint(0, 60) for _ in range(0, 6))
    lista.sort()
    print(lista)
    lista.clear()
    sleep(2)  