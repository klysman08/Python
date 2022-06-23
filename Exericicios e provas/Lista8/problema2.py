def power(base, expoente):
    if expoente == 0:
        return 1
    else:
        return base * exponte_recursivo(base, expoente - 1)
    
base = int(input("Digite k: "))
expoente = int(input("Digite n: "))

print(power(base, expoente))

