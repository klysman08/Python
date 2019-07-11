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



""" 67 tabuada
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

    if ( i >= 18):
        total += 1

    if ( g == 'M'):
        m += 1
    if ( g == 'F'):
        if ( i > 20):
            f += 1  
    
    c = ' '
    while g not in 'SN':
    c = str(input('Deseja registrar outro [S/N]:')).strip().upper()[0]
    
    if( c == 'N'):
        print('Saindo do programa')
        break

    contador += 1

print (f'Total de pessoas cadastradas {contador} || {total} maiores de 18 anos  - {m} Homens e {f} Mulheres > 20 anos') """



"""  # 70 
total = maior = menor = cont = continuar = 0
mil = 0

while True:
    nome = str(input('Qual o nome do produto? '))
    preço = int(input('Qual o preço dele? '))
    cont += 1

    if ( preço >= maior ):
        maior = preço
        nmaior = nome

    if ( cont == 1 ) or ( preço < menor ):
        menor = preço
        nmenor = nome

    
    total += preço

    if ( preço > 1000 ):
        mil += 1


    continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    while continuar not in 'SsNn':
        continuar = str(input('Dados invalidos. tente novamente: '))

    if ( continuar == 'N'):
        break

print('-'*20)
print (f'O total gasto na compra foi {total}\nA quantidade de produtos maiores que 1000 foram {mil}\nO produto mais caro foi {nmaior} custando {maior}\nO mais barato foi {nmenor} custando {menor}')
print('-' * 20)  """



""" # 71 Caixa Eletrônico 
valor = int(input('Qual o valor para sacar? '))

total = valor
ced = 50
totalced = 0

nota50 = valor // 50
valor = valor % 50

print(nota50)
print(valor)

while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cedulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced == 10
        elif ced == 10:
            ced == 1
        elif ced == 1:
            ced = 0
        totalced = 0
        if total == 0:
            break
print('sacar') """