#081
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