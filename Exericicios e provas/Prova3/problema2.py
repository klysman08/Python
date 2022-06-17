def consumo(distancia, quantidade_litros):
    if distancia / quantidade_litros < 8: 
        return print('Venda o carro')
    elif distancia / quantidade_litros <= 12:
        return print('Econômico')
    else:
        return print('Super econômico')
    
retorno = consumo(100,10)
retorno2 = consumo(30, 4.5)
