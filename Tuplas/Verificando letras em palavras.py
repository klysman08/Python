"""  """
#077

linguagens = ('Java', 'C', 'Python', 'C++', 'Visual Basic',
                'JavaScripy', 'C#', 'PHP', 'SQL', 'Objective-C')
i = 0
for i in linguagens:
    print(f'\nNa palavra {i.upper()} temos ', end='')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
