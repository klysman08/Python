import math

valocidade_maxima = int(input("Digite a velocidade máxima: "))
velocidade_registrada = int(input("Digite a velocidade registrada: "))


if velocidade_registrada >= valocidade_maxima*1.2 and velocidade_registrada < valocidade_maxima*1.2:
    print("Infração Média")
    
elif velocidade_registrada >= valocidade_maxima*1.2 and velocidade_registrada < valocidade_maxima*1.5:
    print("Infração Grave")
    
elif velocidade_registrada >= valocidade_maxima*1.5:
    print("Infração Gravíssima")
else:
    print("Sem Infração")