n = 0
soma = 0
pares = 0
impares = 0

while n >= 0:
    n = int(input("Digite um numero: "))
    
    if n < 0:
        break

    if n% 2 == 0:
        pares = pares + n
    else:
        impares = impares + n

print(f'Soma pares:{pares}')
print(f'Soma impares:{impares}')

