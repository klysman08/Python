def estacionamento(horas_chegada, minutos_chegada, hora_saida, minuto_saida):

    minutos1 = horas_chegada* 60 + minutos_chegada
    minutos2= hora_saida * 60 + minuto_saida

    if horas_chegada < hora_saida:
        minutos_totais = minutos2 - minutos1
        horas_totais = minutos_totais // 60
    else:
        minutos_totais = minutos1 - minutos2
        horas_totais = minutos_totais // 60

    if horas_totais <= 2:
        return horas_totais * 1.00
    elif horas_totais >2 and horas_totais <= 4:
        return (horas_totais) * 1.40
    else:
        return horas_totais * 2.00
    
    
retorno = estacionamento(18,50,22,49)
retorno2= estacionamento(20,30,8,0)



def estacionamento(hc, mc, hp, mp):
    minc = hc * 60 + mc
    minp = hp * 60 + mp

    if minp > minc:
        minuto = (minp - minc) % 60
        hora = int((minp - minc) / 60)
    else:
        minuto = ((24 * 60) - minc + minp) % 60
        hora = int(((24 * 60) - minc + minp) / 60)

    if hora < 2 or (hora == 2 and minuto == 0):
        if minuto != 0:
            hora += 1
        return hora
    elif hora < 4 or (hora == 4 and minuto == 0):
        if minuto != 0:
            hora += 1
        return (hora * 1.40)
    else:
        if minuto != 0:
            hora += 1 
        return (hora * 2)
    
    
    