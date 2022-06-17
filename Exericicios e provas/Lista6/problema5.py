'''escreva um programa que leia uma data no formato DD/MM/AAAA e imprima na tela a data no formato MM/DD/AAAA'''

data = input('Digite uma data no formato DD/MM/AAAA: ')

dia = data[0:2]
mes = data[3:5]
ano = data[6:10]

print(f'{mes}/{dia}/{ano}')