def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

def fatorial_while(n):
    f = 1
    while n > 0:
        f *= n
        n -= 1
    return f

print(fatorial(5), fatorial_while(5))