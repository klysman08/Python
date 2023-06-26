from functools import reduce

notas = [5.0, 7.0, 8.0, 9.0, 10.0]

def somar(a, b):
    """
    This function receives two numbers and returns their sum.
    """
    return a + b

total = reduce(somar, notas, 0)

print(total)