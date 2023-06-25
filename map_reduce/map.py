from functools import reduce

def mais_um_e_maio(nota):
    """
    This function receives a grade and returns it increased by 1.5.
    """
    return nota + 1.5

notas = [5.0, 7.0, 8.0, 9.0, 10.0]
notas_finais = map(mais_um_e_maio, notas)

print(list(notas_finais))