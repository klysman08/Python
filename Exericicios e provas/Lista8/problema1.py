def soma_recursiva(m, n):
    if n == m:
        return m
    else:
        return m + soma_recursiva(m+1, n)
    
    
n = soma_recursiva(1, 4)

print(n)