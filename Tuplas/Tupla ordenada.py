#073

linguagens = ('Java', 'C', 'Python', 'C++', 'Visual Basic', 'JavaScripy', 'C#', 'PHP', 'SQL', 'Objective-C')

print('=' * 20)
print(linguagens[:5])
for i in range(0, 5):
    print(linguagens[i])

print('=' * 20)
print(linguagens[-4:])
for i in range(1, 5):
    print(linguagens[-i])

print('=' * 20)
print(sorted(linguagens))  # Exibe em forma de lista ordenada

print('=' * 20)
for count, nome in enumerate(linguagens):
    print(f'Na posição {count+1} temos a liguagem {nome}')

print('=' * 20)
p = linguagens.index('Python')
print(f'Python está na {p+1} º posição')