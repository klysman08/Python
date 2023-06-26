
class Cachorro():

    def __init__(self, raca, cor, tamanho):
        self.raca = raca
        self.cor = cor
        self.tamanho = tamanho


dog1 = Cachorro("Labrador", "Marrom", "2 metro")
dog2 = Cachorro("Vira Lata", "Preto", "1 metro")

print("-" * 20)
print("OBJETO")
print(dog1)
print(dog2)

print("-" * 20)
print("TIPO")
print(type(dog1))
print(type(dog2))

dog1.tamanho = 3

print("-" * 20)
print("Cahorro 1 ")
print("Raça: ", dog1.raca)
print("Cor: ", dog1.cor)
print("Tamanho: ", dog1.tamanho)

print("-" * 20)
print("Cahorro 2 ")
print("Raça: ", dog2.raca)
print("Cor: ", dog2.cor)
print("Tamanho: ", dog2.tamanho)
print("-" * 20)
