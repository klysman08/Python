def serie_harmonica(n):
    soma = 0.0
    for den in range(1,n+1):
        soma = soma + (1.0/den)
        

    return soma

print(serie_harmonica(6))