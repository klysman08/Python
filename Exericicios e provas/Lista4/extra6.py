def escalas(inicio, fim, passo):
    count = 0
    while inicio <= fim:
        celcius = inicio
        fahrenheit = int((celcius * 9/5) + 32)
        kelvin = int(celcius + 273)
        
        print(f'{celcius}, {fahrenheit}, {kelvin}')
        
        inicio = inicio + passo

escalas(20,70,7)