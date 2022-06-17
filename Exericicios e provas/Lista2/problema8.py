
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

if nota1 and nota2 <=10:
    media = (nota1 + nota2) / 2
    print('Média %.2f' %media)
else:
    print('Nota inválida')