
def populacao(A,taxa_a, B, taxa_b):
    i = 0
    while True: #Do while

        A = A*(1+ taxa_a/100)
        B = B*(1+ taxa_b/100)
        i += 1
        
        if A >= B: #while
            break
    
    return i

print(populacao(100, 12, 200000, 2))

