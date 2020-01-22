#085 Matriz
matriz = [[],[],[]]
for i in range(0, 3):
    for j in range(0, 3):
        n = int(input(f'Digite o valor para posição [{i},{j}]: '))
        matriz[i].append(n)
for c in range(0, 3):
    for l in matriz[c]:
        print(f'[{l:^5}]', end='') 