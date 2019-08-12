""" #078
maior = menor = 0
lista = list()
for i in range(0, 5):
    lista.append(int(input('Digite um numero: ')))
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]

for pos, m in enumerate(lista):
    if m == maior:
        print(f'{pos}...')
    elif m == menor:
        print(f'{pos}...')
        
maior = max(lista)
posicao = lista.index(maior)

print(f'O menor valor é: {menor} e o maior valor é {maior} e está na posição {posicao}') """


"""#079
lista = list()
while True:
    n = int(input('Digite um numero: '))

    if n == 0:
        break

    if n in lista:
        print('Esse numero já exite na lista, tente novamente!')
    else:
        lista.append(n)

print(sorted(lista)) 
print(lista) """


""" #080

lista = list()

for i in range(0, 5):
    n = int(input(f'Digite o {i+1} numero: '))

    if i == 0 or n > lista[-1 ]:
        lista.append(n)
        print('Adicionado ao final da lista!')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print(lista) """

""" #081
lista= list()
while True:

    n = int(input('Digite um numero: '))

    if n == 0:
        break
    
    lista.append(n)
lista.sort(reverse=True)
print(lista)

if 5 in lista:
    print(f'O valor 5 está na lista e na posição {lista.index(5)} e lista tem {len(lista)} elementos')
else:
    print('O valor 5 não está na lista') """

""" #082

lista = list()
listapar = list()
listaimpar = list()

while True:
    n = int(input('Digite um número para lista e 0 para sair: '))
    
    if n == 0:
        break
    
    lista.append(n)

for i in range(0, len(lista)):
    if lista[i] % 2 == 0:
        listapar.append(lista[i])
    else:
        listaimpar.append(lista[i])

for i, v in enumerate(lista):
    if v % 2 == 0:
        listapar.append(v)
    else:
        listaimpar.append(v)

print(f'Lista completa {lista}')
print(f'Lista par {listapar}')
print(f'Lista impar {listaimpar}') """



""" #083

espressao = str(input("Digite uma expressão dentro de parenteses: "))

lista = list()

for s in espressao:
    if s == '(':
        lista.append('(')

    elif s == ')':
        if len(lista) > 0:
            lista.pop()

        else:
            lista.append(')')
            break

if len(lista) == 0:
    print('Sua expressão está correta')
else:
    print('Tente novamente') """


""" #084

pessoas = list()
lista = list()

for i in range(0, 3):


    pessoas.append(str(input('Insira o nome:')))
    pessoas.append(int(input('Insira o peso:')))
    lista.append(pessoas[:])
    pessoas.clear()


pesados = list()
magros = list()

for peso in lista:
    if peso[1] >= 80:
        pesados.append(peso)
    elif peso[1] < 80:
        magros.append(peso)

print(len(lista))
print(pesados)
print(magros) """


""" #085
lista = [[],[]]

for c in range(0, 7):
    n = int(input(f'Digite o {c} numero: '))

    if n % 2 == 0:
        lista[0].append(n)

    elif n % 2 == 1:
        lista[1].append(n)

lista[0].sort()
lista[1].sort()

print(lista[0])
print(lista[1]) """


""" #085 Matriz
matriz = [[],[],[]]
for i in range(0, 3):
    for j in range(0, 3):
        n = int(input(f'Digite o valor para posição [{i},{j}]: '))
        matriz[i].append(n)
for c in range(0, 3):
    for l in matriz[c]:
        print(f'[{l:^5}]', end='') """

""" #086

matriz = [[],[],[]]
for i in range(0,4):
    for j in range(0, 3):
        n = int(input(f'Insira a posição [{i},{j}]: '))
        matriz[i].append(n)

soma = 0
soma2 = 0
maior = menor = 0

for c in range(0, 3):
    for l in matriz[c]:
        print(f'[{l:^5}]', end=' ')
        
        if l % 2 == 0:
            soma += l

    if c == 1:
        maior = menor = matriz[1][c]
        
    elif matriz[1][c] > maior:
        maior = matriz[1][c]

    soma2 += matriz[c][2]

    print()

print(soma) #soma dos valores pares
print(soma2) #soma dos valores da 3 coluna
print(maior) # maior valor da segunda linha """

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
