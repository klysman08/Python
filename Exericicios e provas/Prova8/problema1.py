dicionario_RNA = {'UUU':'Phe', 'CUU': 'Leu', 'UUA': 'Leu', 'AAG': 'Lisina','UCU':'Ser', 'UAU': 'Tyr', 'CAA':'Gln'}
rna = str(input('Digite o RNA: '))
n = len(rna) // (len(rna) // 3 )
lista = [rna[index: index + n] for index in range(0, len(rna), n)]
transcricao = [dicionario_RNA[k] for k in lista if k in dicionario_RNA]
print(lista)
print(transcricao)

## ---------------------------------------------------------------

cd = input('Digite o RNA: ')
rna = {'UUU': 'Phe', 'CUU': 'Leu', 'UUA': 'Leu' ,'AAG': 'Lisina', 'UCU': 'Ser', 'UAU': 'Tyr', 'CAA': 'Gln'}
ami = ''
for i in range(0, len(cd), 3):
    ami = ami + rna[cd[i:i+3]] + '-'
print('Cadeia de Aminoácidos:', ami[:-1])