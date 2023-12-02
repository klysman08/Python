#078
maior = menor = 0
lista = []
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
    if m in [maior, menor]:
        print(f'{pos}...')
maior = max(lista)
posicao = lista.index(maior)

print(f'O menor valor é: {menor} e o maior valor é {maior} e está na posição {posicao}') 