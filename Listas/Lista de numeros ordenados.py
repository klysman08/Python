from random import randint
from time import sleep


n = int(input('Quantos jogos devem ser gerados? '))
lista = list()
for i in range(0, n):
    for c in range(0, 6):
        lista.append(randint(0, 60))
    
    lista.sort()
    print(lista)
    lista.clear()
    sleep(2)  