'''
#Contar até N usando while
n = int(input("Digite um numero para contar de 0 até ele: "))

count = 1

while count < n:
    count += 1
    count = count + 1

print("Resultado {}".format(count))

'''
'''
#Fatorial usando a biblioteca
f = int(input("Digite um numeoo para calcular o fatorial dele: "))
resultado = math.factorial(f)
print(resultado)

#Fatorial usando While
count = 1
e = 1
while count <= f:
    e = e*count
    count += 1
resultado2 = e
print("O resultado do fatarial digitado é: {}".format(resultado2))

#Fatorial usando for
n = int(input('Digite um numero para calcaular o FAT: '))
s = 1
for c in range(1, n+1):
    s = s*c
print("O resultado do fatarial digitado é: {}".format(s))

'''



'''#Soma de todos os impares de 1 a 100
soma = 0
for c in range (1, 100):
    if (c % 2 == 1):
        soma +=c
print(soma)
'''

'''#Soma de todos os n de 1 a n - Formula
r = 2
n = int(input('Digite o número n: '))'''


'''
if ( n % 2 == 0):
    soma = ((1+n)*n)/2
else:
    soma = (n+1)*(n//2) + (n+1)/2

print(soma)
'''