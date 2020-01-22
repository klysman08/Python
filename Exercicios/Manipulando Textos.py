cid = str(input('Sua Cidade: ')).strip()
print(cid[:5].upper() == 'Santo')

n = str(input('Qual seu nome')).strip()
print('Seu nome tem Silva? {}'.format('silva' in n.lower()))


f = str(input('Digite uma frase:')).strip().upper()
print(f.count('A'))
print('A primeira letra a da frase se encontra na posição {} e a ultima está na posição {}'.format(f.find('A'), f.rfind('A')))

nome = str(input('Digite seu nome')).strip()
n = nome.split()
print('Seu primeiro nome é {}, e seu ultimo nome é {}'.format(n[0],n[-1]))
