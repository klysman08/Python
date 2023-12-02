v = int(input('Qual a velocidade do carro: '))
if v >= 50:
    print('Você foi multado')
    m = v - 50
    print(f'Você deve pagar uma multa no valor de {m * 7} reais')
else:
    print('Tudo certo')