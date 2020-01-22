contador = soma = 0
while True:
    n = int(input('Digite qualquer número e 999 para sar: '))
    
    if (n == 999):
        break

    soma += n
    contador += 1

print(f'A soma dos numeros digitados foi {soma} e quantidade digitada foi {contador}')