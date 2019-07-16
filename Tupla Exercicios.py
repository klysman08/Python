numero = ('um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
c = 0
while True:
    c = int(input('Digite um numero:'))
    
    if c > 10 or c < 0:
        print('Somente números de 0 a 10')
        
    if c > 0 and c < 20:
        print(numero[c-1])

