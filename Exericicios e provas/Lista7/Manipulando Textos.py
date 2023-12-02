cid = str(input('Sua Cidade: ')).strip()
print(cid[:5].upper() == 'Santo')

n = str(input('Qual seu nome')).strip()
print(f"Seu nome tem Silva? {'silva' in n.lower()}")


f = str(input('Digite uma frase:')).strip().upper()
print(f.count('A'))
print(
    f"A primeira letra a da frase se encontra na posição {f.find('A')} e a ultima está na posição {f.rfind('A')}"
)

nome = str(input('Digite seu nome')).strip()
n = nome.split()
print(f'Seu primeiro nome é {n[0]}, e seu ultimo nome é {n[-1]}')
