from getpass import getpass

palavra_secreta = str(getpass("Qual a palavra secreta?").upper())

tracos = list(palavra_secreta)
exibicao_lista = ["_" for _ in tracos]
cont = len(palavra_secreta)

tentativas = 0
letra = 0
erros = 0

tentativas_lista = []

while (cont != 0 and letra != 'sair' and erros <= 5):
    print(" ".join(exibicao_lista))

    print("Tentativas até agora:\n", tentativas_lista)

    letra = str(input('Seu palpite: '))

    # Deveremos verificar se a letra existe na palavra secreta e alterar as variáveis declaradas até então
    # Insira sua lógica a seguir:
    if letra.upper() in tentativas_lista:
        print(f'A letra {letra.upper()} já foi utilizada')


    else:
        busca = 0
        for i in range(0, len(palavra_secreta)):
            if letra.upper() == palavra_secreta[i]:
                exibicao_lista[i] = letra.upper()
                cont -= 1
                busca = 1
        if busca == 0:
            erros += 1
            print("Não há.")
        tentativas += 1
        tentativas_lista.append(letra.upper())
        tentativas_lista.sort()




    # Fim da sua lógica

if letra == "sair":
    print("Obrigado, até mais!")
elif erros > 5:
    print("Você foi enforcado. :(")
else:
    print(" ".join(exibicao_lista))
    print(
        f"Parabéns, você advinhou que a palavra é {palavra_secreta}"
        + f" depois de {tentativas} tentativas."
    )


