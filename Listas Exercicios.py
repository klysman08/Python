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


#079
""" lista = list()
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


#80

""" lista = list()

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

#81
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
    print('O valor 5 não está na lista')
