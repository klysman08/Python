
 while True:
    n = int(input('Digite um numero para a sua tabuada: '))
    i = 0
    
    if n < 0:
        print("Somente números positivos")
        print('Saindo do programa...')
        break
    
    while (i <= 9):
            print (f' {n} x {i} = {n*i}')
            i += 1