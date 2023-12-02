with open("texto.txt", 'r') as arquivo:
    data = []
    datas = []

    for l in arquivo:
        dia, mes, ano = l.split('/')
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)
        data = [ano, mes, dia]
        datas.append(data)

    datas_mais_recente = max(datas)

    ano, mes, dia = datas_mais_recente

    print(f'{dia}/{mes}/{ano}')