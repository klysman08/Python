def tabuada(n):
    print(f'Tabuada de {n}')
    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')
        

n = int(input('Digite um inteiro: '))

tabuada(n)