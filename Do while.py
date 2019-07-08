#Estrutura de repecição com condição de parada

""" while True:
    print('Olá mundo')
    break """


####################################

#EXERCICIOS

# 66

""" contador = soma = 0
while True:
    n = int(input('Digite qualquer número e 999 para sar: '))
    
    if (n == 999):
        break

    soma += n
    contador += 1

print(f'A soma dos numeros digitados foi {soma} e quantidade digitada foi {contador}')
 """



""" 67
 while True:
    n = int(input('Digite um numero para a sua tabuada: '))
    i = 0
    
    if n < 0:
        print("Somente números positivos")
        print('Saindo do programa...')
        break
    
    while (i <= 9):
            print (f' {n} x {i} = {n*i}')
            i += 1 """



""" 68
contador = 0
from random import randint
while True:
    c = randint(0,10)
    n = int(input('1 para Par ou 2 para Impar: '))
    e = int(input('Escolha seu número: '))

    if ( n == 1):
        if ( (e+c) % 2 == 0 ):
            print('Deu par!')
            print(f'Você escolheu {e} e o Pc escolheu {c}')
            print('Você ganhou!')
        else:
            print('Você perdeu!')
            break

    if ( n == 2):
        if ((e+c) % 2 == 1):
            print('Deu impar')
            print(f'Você escolheu {e} e o Pc escolheu {c}')
            print('Você ganhou!')
        else:
            print('Você perdeu!')
            break

    contador += 1

print(f'Numero de tentativas: {contador}') """


 # 69 
""" total = m = f = contador =  0

while True:

    i = int(input('Qual a sua idade: '))

    g = ' '
    while g not in 'MF':
        g = str(input('Qual seu género: ')).strip().upper()[0]

    if ( i > 18):
        total += 1

    if ( g == 'M'):
        m += 1
    if ( g == 'F'):
        if ( i > 20):
            f += 1     

    c = str(input('Deseja registrar outro [S/N]:')).strip().upper()[0]
    
    if( c == 'N'):
        print('Saindo do programa')
        break

    contador += 1

print (f'Total de pessoas cadastradas {contador} || {total} maiores de 18 anos  - {m} Homens e {f} Mulheres > 20 anos') """




