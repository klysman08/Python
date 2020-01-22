
# 65 media maior e menor
contador = 0
soma = 0
n = 1

while (n != 0):
    n = int(input('Digite um numero qualquer e 0 para o resultado: '))
    if ( n != 0 ):
        soma += n
        contador += 1
        if (contador == 1):
            n = maior = menor = 1
        else:
            if (n > maior):
                maior = n
            if (n < menor):
                menor = n

media = soma / contador
print('A média de todos o valores digitados é: {}'.format(media))
print(f'O menor valor digitado foi {menor} e o maior for {maior}')
