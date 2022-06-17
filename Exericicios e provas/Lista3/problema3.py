def verifica_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

def tipo_triangulo(a, b, c):
    if a == b == c:
        return 'Equilátero'
    elif a == b or a == c or b == c:
        return 'Isosceles'
    else:
        return 'Escaleno'
    
