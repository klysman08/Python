def ocorrencia_letras(palavra):
    dicionario = {}
    for letra in palavra:
        dicionario[letra] = dicionario.get(letra, 0) + 1
        
    elementos = []
    
    for letra, contador in dicionario.items():
        elementos.append((contador, letra ))
        
        letra_mais_frequente, valor = max(elementos)
            
    return letra_mais_frequente


palavra = input('Digite uma palavra:')
print(ocorrencia_letras(palavra))