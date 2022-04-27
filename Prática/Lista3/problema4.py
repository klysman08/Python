
def calcula_valor(preço, quantidade_de_litros, tipo_combustivel):
    if tipo_combustivel == 'A' or tipo_combustivel == 'a':
        if quantidade_de_litros <= 20:
            preço_total = preço * quantidade_de_litros * 0.97
        else:
            preço_total = preço * quantidade_de_litros * 0.95
            
    elif tipo_combustivel == 'B' or tipo_combustivel == 'b':
        if quantidade_de_litros <= 20:
            preço_total = preço * quantidade_de_litros * 0.96
        else:
            preço_total = preço * quantidade_de_litros * 0.94
            
    return preço_total

print(calcula_valor(2.5, 10, 'A'))

#(quantidade_de_litros, tipo_combustivel, preço):