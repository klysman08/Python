
a = 0
contador = 0
soma = 0

while (a != 999):
    a = int(input('Digite um numero: '))
    if ( a != 999):
        soma += a

    contador += 1

print(
    f'A quantidade de numeros digitados foi {contador - 1} e a soma deles é {soma}'
) 