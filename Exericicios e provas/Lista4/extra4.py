

while True:
    
    
    print('1. Adição')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    print('5. Saida')

    n = int(input('Digite um número: '))
    if n == 5:
        break

    if n == 1:
        x = int(input('Digite um número: '))
        y = int(input('Digite um número: '))
        print('1. Adição =', x + y)
    elif n == 2:
        x = int(input('Digite um número: '))
        y = int(input('Digite um número: '))
        print('2. Subtração =', x - y)
    elif n == 3:
        x = int(input('Digite um número: '))
        y = int(input('Digite um número: '))
        print('3. Multiplicação =', x * y)
    elif n == 4:
        x = int(input('Digite um número: '))
        y = int(input('Digite um número: '))
        print('4. Divisão =', x / y)
    
    