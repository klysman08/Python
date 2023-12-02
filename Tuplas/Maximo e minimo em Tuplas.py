#074
from random import randint
tupla = ((randint(0, 10), randint(0, 10), randint(0, 10),
        randint(0, 10), randint(0, 10), randint(0, 10)))
lista = [randint(0, 10) for _ in range(0,6)]
print(lista)
print(tupla)

maximo = 0
menor = 0

for k in range(0, len(tupla)):
    if maximo <= tupla[k]:
        maximo = tupla[k]

    if (k == 1) or tupla[k] <= menor:
        menor = tupla[k]

print(maximo)
print(max(tupla))
print(min(tupla))
print(menor)