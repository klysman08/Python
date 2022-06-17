idade = int(input("Digite a idade: "))
tempo = int(input("Digite o tempo de contrubuição: "))
sexo = str(input("Digite o sexo: "))

if idade >= 60 and tempo <= 35 and sexo == "M":
    print("Pode aposentar")
elif idade >= 60 and tempo <= 30 and sexo == "F":
    print("Pode aposentar")
else:
    print("Não pode aposentar")
