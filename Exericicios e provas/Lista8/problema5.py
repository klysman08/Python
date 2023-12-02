def imprime_naturais(n):
    if n == 0:
        return print(n)
    imprime_naturais(n-1)
    print(n)
        

n = int(input("Digite N: "))
print(imprime_naturais(n))
