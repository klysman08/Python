n = -2
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