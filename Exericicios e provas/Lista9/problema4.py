while True:
    numero = int(input('Digite um número: '))

    if numero == -1:
        break

    dicionario = {}

    dicionario[numero] = dicionario.get(numero, 0) + 1

lista = [(v, n) for n, v in dicionario.items()]
for i, j in lista:
    print(f'{j} - {i}')

print(dicionario)
print(lista)

