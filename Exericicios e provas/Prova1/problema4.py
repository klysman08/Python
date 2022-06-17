numero = int(input('Digite um número de 4 algarismos: '))

algarismo1 = numero // 1000
algarismo2 = numero % 1000 // 100
algarismo3 = numero % 100 // 10
algarismo4 = numero % 10

soma = algarismo1 + algarismo2 + algarismo3 + algarismo4

print(soma)