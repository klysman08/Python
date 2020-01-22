#072
numero = ('zero','um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
c = 0
while True:
    c = int(input('Digite um numero:'))
        
    if c >= 0 and c <= 10:
        print(numero[c])

    else:
        print('Somente números de 0 a 10')