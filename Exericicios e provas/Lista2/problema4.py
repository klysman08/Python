
REAJUSTE20 = 0.2
REAJUSTE15 = 0.15
REAJUSTE10 = 0.1
REAJUSTE5 = 0.05

salario = float(input("Salário: "))

if salario <= 280:
    aumento = salario * REAJUSTE20
    novo_salario = salario + aumento
elif salario > 280 and salario <= 700:
    aumento = salario * REAJUSTE15
    novo_salario = salario + aumento
elif salario > 700 and salario <= 1500:
    aumento = salario * REAJUSTE10
    novo_salario = salario + aumento
elif salario > 1500:
    aumento = salario * REAJUSTE5
    novo_salario = salario + aumento

print ('Valor do aumento: %.2f' % aumento)
print('Novo salário %.2f' %novo_salario)
