#074
from random import randint
lista = []
tupla = ((randint(0, 10), randint(0, 10), randint(0, 10),
        randint(0, 10), randint(0, 10), randint(0, 10)))
for i in range(0,6):
    lista.append(randint(0, 10))


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