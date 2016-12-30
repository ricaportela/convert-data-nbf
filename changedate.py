""" Calcular Data a partir de uma quantidade de minutos """


def alterar_data(xdataEnt, xop, xminutosEnt):
    """ Calcular nova data """
    dataEnt, horaEnt = xdataEnt.split(" ", 2)
    diaEnt, mesEnt, anoEnt = xdataEnt.split("/", 3)
    horaEnt, minuEnt = horaEnt.split(":", 2)

    # transformar tudo em minutos
    # converter horas em minutos totais
    minutosTotais = (int(horaEnt) * 60) + int(minuEnt) + xminutosEnt

    # 5415 / 60 minutos = 90.25 => separar inteiro de casas decimais 0.25 * 60  = 15
    # HORAS_CONV_MINUTOS = MIN_TOT_E / 60

    # 90h e 15 min
    # I, D = divmod(HORAS_CONV_MINUTOS, 1)
    # RESTO_MINUTOS = D * 60

    # 90h / 24h = 3.75 => separar inteiro de casas decimais = 0.75 / 24
    # TOTAL_DIAS = QTDE_TOTAL_HORAS / 24

    # I, D = divmod(TOTAL_DIAS, 1)

    # 3d 3.75 (0.75 * 24)  = 18 h
    # TOTAL_HORAS2 = D * 24

    # print(int(I), " Dias", int(TOTAL_HORAS2), " horas", int(TOTAL_MINUTOS), " minutos")
    print("Total de Minutos: ", minutosTotais)
    return minutosTotais


if __name__ == ("__main__"):
    alterar_data("31/12/2016 23:35", "+", 4000)

