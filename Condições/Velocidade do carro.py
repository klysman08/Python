v = int(input('Qual a velocidade do carro: '))
if  v >= 50:
    print('Você foi multado')
    m = v - 50
    print('Você deve pagar uma multa no valor de {} reais'.format(m*7))
else:
    print('Tudo certo')