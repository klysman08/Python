def soma_recursiva(m, n):
    return m if n == m else m + soma_recursiva(m+1, n)
    
    
n = soma_recursiva(1, 4)

print(n)

"test git repli.it"