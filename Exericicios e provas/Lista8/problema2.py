def power(base, expoente):
    return 1 if expoente == 0 else base * exponte_recursivo(base, expoente - 1)
    
base = int(input("Digite k: "))
expoente = int(input("Digite n: "))

print(power(base, expoente))

