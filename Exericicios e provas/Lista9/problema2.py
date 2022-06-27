vogais = ['a', 'e', 'i', 'o', 'u']

palavra = input('Digite uma palavra: ')

lista = []

def vogais_soma_palavra(palavra):
    for i in palavra:
        if i in vogais:
            lista.append(i)
    return max(lista, key=lista.count)

print(vogais_soma_palavra(palavra))