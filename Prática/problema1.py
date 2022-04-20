#programa para calcular o raio de uma circuferencia, area da circuferencia e volume da esfera

def calcula_raio(raio):
    
    #raio = int(input("Digite o valor do raio da circunferência: "))

    perimetro = 2 * 3.1415 * raio
    area = 3.1415 * (raio**2)
    volume = (4/3) * 3.1415 * (raio**3)
    

    print('Perímetro:', perimetro.__format__('0.2f'))
    print('Área:', area.__format__('0.2f'))
    print('Volume:', volume.__format__('0.2f'))
    
    return perimetro, area, volume

resultado = calcula_raio(5)

print(resultado)

def testa_resultado ():
    assert calcula_raio(5) == (3211.415000000000003, 78.53750000000001, 523.5833333333333), "Erro, nao passou no teste"

testa_resultado()