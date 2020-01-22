#086

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
print(maior) # maior valor da segunda linha 