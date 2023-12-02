def imprime_naturais_impares(n):
    if n == 1:
        return print(n)
    if n % 2 != 0:
        print(n)
    imprime_naturais_impares(n-1)

n = int(input("Digite N: "))
print(imprime_naturais_impares(n))