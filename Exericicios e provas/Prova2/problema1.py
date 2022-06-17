
dig1 = int(input('Digite o primeiro número: '))
dig2 = int(input('Digite o segundo número: '))
dig3 = int(input('Digite o terceiro número: '))


if dig1 > dig2 and dig1 > dig3:
    maior = dig1
    if dig2 > dig3:
        menor = dig3
        mediana = dig2
    else:
        menor = dig2
        mediana = dig3
elif dig2 > dig1 and dig2 > dig3:
    maior = dig2
    if dig1 > dig3:
        menor = dig3
        mediana = dig1
    else:
        menor = dig1
        mediana = dig3
else:
    maior = dig3
    if dig1 > dig2:
        menor = dig2
        mediana = dig1
    else:
        menor = dig1
        mediana = dig2
    
print('Mediana: {}'.format(mediana))
