soma = 0
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if (n % 2 == 0):
        soma = soma + n
print(soma)