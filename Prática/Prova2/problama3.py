valor_hora_trabalho = float(input('Digite o valor da hora trabalhada: '))
quantidade_hora_trabalhada_mes = float(input('Digite a quantidade de horas trabalhadas no mês: '))

salario_bruto = valor_hora_trabalho * quantidade_hora_trabalhada_mes

if salario_bruto <= 900:
    inss = salario_bruto * 0.1
    fgts = salario_bruto * 0.11
    imposto_de_renda = 0
elif salario_bruto > 900 and salario_bruto <= 1500:
    inss = salario_bruto * 0.1
    fgts = salario_bruto * 0.11
    imposto_de_renda = salario_bruto * 0.05
elif salario_bruto > 1500 and salario_bruto <= 2500:
    inss = salario_bruto * 0.1
    fgts = salario_bruto * 0.11
    imposto_de_renda = salario_bruto * 0.1
else:
    inss = salario_bruto * 0.1
    fgts = salario_bruto * 0.11
    imposto_de_renda = salario_bruto * 0.2

salario_liquido_total = salario_bruto - inss - imposto_de_renda

print('Salário Bruto: R$ %.2f' % salario_bruto)
print('IR: R$ %.2f' % imposto_de_renda)
print('INSS: R$ %.2f' % inss)
print('FGTS: R$ %.2f' % fgts)
print('Total dos descontos: R$ %.2f' % (inss + imposto_de_renda))
print('Salário Líquido: R$ %.2f' % salario_liquido_total)


