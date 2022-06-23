#teste

def exponte_recursivo(base, expoente):
    if expoente == 0:
        return 1
    else:
        return base * exponte_recursivo(base, expoente - 1)
    
base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

print(exponte_recursivo(base, expoente))
