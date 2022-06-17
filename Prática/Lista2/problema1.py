""" import math

lista = []
for i in range(0, 5):
    lista.append(int(input("Digite um número: ")))

max = max(lista)
min = min(lista)
divisiveis = 0

#verifica se o número é divisível por 3
for i in range(0, len(lista)):
    if lista[i] % 3 == 0:
        divisiveis = divisiveis + 1

print('Maior',max)
print('Min',min)
print('divisiveis',divisiveis) """
        

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))
num4 = int(input("Digite um número: "))
num5 = int(input("Digite um número: "))

maior = num1
menor = num1
divisível = 0

if num2 > maior:
    maior = num2
if num2 < maior:
    menor = num2

if num3 > maior:
    maior = num3
if num3 < menor:
    menor = num3

if num4 > maior:
    maior = num4
if num4 < menor:
    menor = num4

if num5 > maior:
    maior = num5
if num5 < menor:
    menor = num5

if num1 % 3 == 0:
    divisível = divisível + 1
if num2 % 3 == 0:
    divisível = divisível + 1
if num3 % 3 == 0:
    divisível = divisível + 1
if num4 % 3 == 0:
    divisível = divisível + 1
if num5 % 3 == 0:
    divisível = divisível + 1



print('Maior:',maior)
print('Menor:',menor)
print('Quantidade de divisíveis por 3:',divisível)