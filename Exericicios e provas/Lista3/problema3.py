def verifica_triangulo(a, b, c):
    return a + b > c and a + c > b and b + c > a

def tipo_triangulo(a, b, c):
    if a == b == c:
        return 'Equilátero'
    elif a == b or a == c or b == c:
        return 'Isosceles'
    else:
        return 'Escaleno'
    
