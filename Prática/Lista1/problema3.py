
tempo_em_segundos = int(input("Digite o valor do tempo em segundos: "))

#converter segundos em horas, minutos e segundos

horas = tempo_em_segundos // 3600
minutos = (tempo_em_segundos % 3600) // 60
segundos = (tempo_em_segundos % 3600) % 60

print("Valor convertido:", int(horas), "h,", int(minutos), "min", int(segundos), "s")
