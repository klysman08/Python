i = j = 0
string1 = input('Digite a primeira string: ')
string2 = input('Digite a segunda string: ')
resultado = ""
while i < len(string1) and j < len(string2):
    resultado += string1[i] + string2[j]
    i+=1
    j+=1
    
while i < len(string1):
    resultado += string1[i]
    i += 1
while j < len(string2):
    resultado += string2[j]
    j += 1

print(f'Combinação:{resultado}')