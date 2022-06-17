dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

ano_bissexto = ano % 4

if (ano%4==0 and ano%100!=0) or (ano%400==0):
    if dia > 31 or mes > 12 or ano < 0:
        print('Data inválida')
    elif dia > 29 and mes == 2:
        print('Data inválida')
    elif dia > 30 and mes == 4 or mes == 6 or mes == 9 or mes == 11:
        print('Data inválida')
    else:
        print('Data válida')
        
elif dia > 31 or mes > 12 or ano < 0:
    print('Data inválida')
elif dia > 28 and mes == 2:
    print('Data inválida')
elif dia > 30 and mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print('Data inválida')
else:
    print('Data válida')
    