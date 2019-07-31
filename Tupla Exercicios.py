""" #072
numero = ('zero','um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
c = 0
while True:
    c = int(input('Digite um numero:'))
        
    if c >= 0 and c <= 10:
        print(numero[c])

    else:
        print('Somente números de 0 a 10') """

""" #73

linguagens = ('Java', 'C', 'Python', 'C++', 'Visual Basic', 'JavaScripy', 'C#', 'PHP', 'SQL', 'Objective-C')

print('='*20)
for i in range(0, 5):
    print(linguagens[i])

print('=' * 20)
for i in range(1, 5):
    print(linguagens[-i])

print('=' * 20)
print(sorted(linguagens))  # Exibe em forma de lista ordenada

print('=' * 20)
for count, nome in enumerate(linguagens):
    print(f'Na posição {count+1} temos a liguagem {nome}')

print('=' * 20)
p = linguagens.index('Python')
print(f'Python está na {p+1} º posição') """


""" #074
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
print(menor) """



""" #075

t1 = (int(input('Digite o 1 numero: ')),)
t2 = (int(input('Digite o 2 numero: ')),)
t3 = (int(input('Digite o 3 numero: ')),)
t4 = (int(input('Digite o 4 numero: ')),)
tupla = t1 + t2 + t3 + t4
print(tupla)

print(tupla.count(9))

if 3 in tupla:
    print(tupla.count(3))
    print(tupla.index(3))
else:
    print('Nenhum numero 3 digitados')

count = 0
lista = []

print('Numeros pares digitados: ')
for i in range(0, len(tupla)):
    if tupla[i] % 2 == 0:
        print(tupla[i])
print(count) """


""" #076

produtos = ('pao', 3, 'leiteee', 3, 'queijo', 5, 'requeijão', 5, 'suco', 3, 'macarrao', 3)

for i in range(0, len(produtos)):
        if (i % 2) == 0:
            print(f'{produtos[i]}')

        else:
            print(f'..................{produtos[i]} R$') """


