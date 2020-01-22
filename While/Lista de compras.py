# 70 
total = maior = menor = cont = continuar = 0
mil = 0

while True:
    nome = str(input('Qual o nome do produto? '))
    preço = int(input('Qual o preço dele? '))
    cont += 1

    if ( preço >= maior ):
        maior = preço
        nmaior = nome

    if ( cont == 1 ) or ( preço < menor ):
        menor = preço
        nmenor = nome

    
    total += preço

    if ( preço > 1000 ):
        mil += 1


    continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    while continuar not in 'SsNn':
        continuar = str(input('Dados invalidos. tente novamente: '))

    if ( continuar == 'N'):
        break

print('-'*20)
print (f'O total gasto na compra foi {total}\nA quantidade de produtos maiores que 1000 foram {mil}\nO produto mais caro foi {nmaior} custando {maior}\nO mais barato foi {nmenor} custando {menor}')
print('-' * 20)  