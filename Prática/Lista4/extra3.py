n = 0
count = 0
media = 0

while True:
    n = int(input("Digite um número: "))
    if n > 0:
        media = media + n
        count += 1
    if n == 0:
        media = media / count
        break
    
print(media)