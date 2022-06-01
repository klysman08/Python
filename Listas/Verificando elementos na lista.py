#079
lista = list()
while True:
    n = int(input('Digite um numero: '))

    if n == 0:
        break

    if n in lista:
        print('Esse numero já existe na lista, tente novamente!')
    else:
        lista.append(n)

print(sorted(lista)) 
print(lista) 