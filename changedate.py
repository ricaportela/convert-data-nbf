""" Calcular Data a partir de uma quantidade de minutos """


def change_date(date, op, value):
    """ Calcular nova data """
    dataEnt, horaEnt = date.split(" ", 2)
    diaIni, mesIni, anoIni = dataEnt.split("/", 3)
    horaIni, minuIni = horaEnt.split(":", 2)

    # transformar tudo em minutos
    # converter horas em minutos totais
    minutosTotais = (int(horaIni) * 60) + int(minuIni) + value
    print("Total de Minutos: ", minutosTotais)

    # 5415 / 60 minutos = 90.25 => separar inteiro de casas decimais 0.25 * 60  = 15
    horas_minutos_conv = minutosTotais / 60
    print(int(horas_minutos_conv))

    # 90h e 15 min
    i, d = divmod(horas_minutos_conv, 1)
    resto_minutos = d * 60
    print(int(resto_minutos))

    # 90h / 24h = 3.75 => separar inteiro de casas decimais = 0.75 / 24
    total_dias = horas_minutos_conv / 24
    print(total_dias)
    i, d = divmod(total_dias, 1)
    xtotal_dias = i
    xtotal_minutos = d
    print("Total Dias", int(xtotal_dias))

    # 3d 3.75 (0.75 * 24)  = 18 h
    minutosHora = xtotal_minutos * 24

    print(int(xtotal_dias), " Dias", int(minutosHora), " horas", int(resto_minutos), " minutos")

    diaIni = int(diaIni) + int(xtotal_dias)
    if diaIni > 30:
       mesIni = int(mesIni) +  1
       diaIni = diaIni - 30

       if mesIni > 12:
          mesIni = 1
       else:
          mesIni += 1
    
    dataSaida = str(int(diaIni)) + "/" + str(mesIni) + "/" + str(anoIni) + " " + str(int(minutosHora)) + ":" + str(int(resto_minutos))
    print(dataSaida)
    

    # data_alterada = '01/01/2012 12:00' essa data sera calculada
    # print(data_alterada)


if __name__ == ("__main__"):
    change_date("01/01/2010 23:35", "+", 90000)

