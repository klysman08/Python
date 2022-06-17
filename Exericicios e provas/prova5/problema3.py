s = input('Frase embaralhada:')
s1 = s[:len(s)//2]
s2 = s[len(s)//2:]

s3 = s1[::-1]
s4 = s2[::-1]

s5 = s3 + ' ' + s4

print(f'Frase correta: {s5}')