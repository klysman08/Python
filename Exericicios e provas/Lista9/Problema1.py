palavra = input('Digite uma palavra: ')

def letra_com_maior_numero_ocorrencia(palavra):
    lista = []
    for i in palavra:
        lista.append(i)
    return max(lista, key=lista.count)


print(letra_com_maior_numero_ocorrencia(palavra))