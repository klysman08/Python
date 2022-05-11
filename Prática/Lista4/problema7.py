
n = 0
soma = 0
while n >= 0:
    n = int(input("Digite um numero: "))
    
    if n < 0:
        break

    soma = soma + n

print(f'Soma:{soma}')