
# 71 Caixa Eletrônico 
valor = int(input('Qual o valor para sacar? '))

total = valor
ced = 50
totalced = 0

nota50 = valor // 50
valor %= 50

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
print('sacar')