total = m = f = contador =  0

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

print (f'Total de pessoas cadastradas {contador} || {total} maiores de 18 anos  - {m} Homens e {f} Mulheres > 20 anos')