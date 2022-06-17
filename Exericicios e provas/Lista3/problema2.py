
def pagamento(valor_hora_trabalho, quantidade_hora_trabalhada_mes):
    
    salario_bruto = valor_hora_trabalho * quantidade_hora_trabalhada_mes
    
    if salario_bruto <= 900:
        imposto_de_renda = 0
        
    elif salario_bruto <= 1500:
        imposto_de_renda = salario_bruto * 0.05
        
    elif salario_bruto <= 2500:
        imposto_de_renda = salario_bruto * 0.1
        
    else:
        imposto_de_renda = salario_bruto * 0.2

    salario_liquido_total = salario_bruto - imposto_de_renda
    
    """ print('Salário Bruto: %.2f' % salario_bruto)
    print('Desconto: %.2f' % imposto_de_renda)
    print('Salario Líquido: %.2f' % salario_liquido_total) """
    
    return salario_bruto, imposto_de_renda, salario_liquido_total
    
valor_hora_trabalho = float(input('Digite o valor da hora trabalhada: '))
quantidade_hora_trabalhada_mes = float(input('Digite a quantidade de horas trabalhadas no mês: '))

pagamento(valor_hora_trabalho, quantidade_hora_trabalhada_mes)


