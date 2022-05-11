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


n = 0
count = 0
media = 0

while n != 0:
    n = int(input("Digite um número: "))
    if n > 0:
        media = media + n
        count += 1
    if n == 0:
        media = media / count
        break
    
print(count, media)