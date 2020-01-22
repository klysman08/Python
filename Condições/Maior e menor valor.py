d = float(input('Qual a distancia da sua viagem? '))
if  d <= 200:
    print('O valor da sua viagem ficou em {:.f} reais '.format(d*0.5))
else:
    print('O valor da sua viagem, como promoção, ficou {:.2f} reais '.format((d*0.45)))

a = int(input('Digite o priemiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > a:
    maior = a
if c > a and c > b:
    maior = c

print('O maior valor é {} e o menor valor é {} '.format(maior, menor))

n = [a,b,c]
print('O maior valor é {} e o menor valor é {} '.format(max(n),min(n)))