temperaturas_mes = []

for i in range(0,12):
    valor = int(input(f'Digite a temperatura do mês {i}: '))
    temperaturas_mes.append(valor)
    
media = sum(temperaturas_mes) / len(temperaturas_mes)

print(f'Média: {media:.2f}')

for j in temperaturas_mes:
    if j > media:
        print(f'{j}')
        
        