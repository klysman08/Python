def imprime_naturais_pares(n):
    if n == 0:
        return print(n)
    imprime_naturais_pares(n-1)
    if n % 2 == 0:
        print(n)

n = int(input("Digite N: "))
print(imprime_naturais_pares(n))