""" Calcular Data a partir de uma quantidade de minutos """
from gregtojulian import gregtojulian
from juliantogreg import juliantogreg
import datetime


def change_date(date, op, value):
    """ Calcular nova data """
    dataEnt, horaEnt = date.split(" ", 2)
    diaIni, mesIni, anoIni = dataEnt.split("/", 3)
    horaIni, minuIni = horaEnt.split(":", 2)
    # convert all to minutes
    # convert hours in minutes to adding in total minutes
    minutosTotais = (int(horaIni) * 60) + int(minuIni) + value
    print("Total de Minutos: ", minutosTotais)
    # 5415 / 60 minutos = 90.25 => separate integer from decimal places 0.25 * 60  = 15
    horas_minutos_conv = minutosTotais / 60
    # 90h e 15 min - i = integer part and d = decimal part
    i, d = divmod(horas_minutos_conv, 1)
    resto_minutos = d * 60
    # 90h / 24h = 3.75 => separate integer from decimal places = 0.75 / 24
    total_dias = horas_minutos_conv / 24
    i, d = divmod(total_dias, 1)
    xtotal_dias = i
    xtotal_minutos = d
    # 3d 3.75 (0.75 * 24)  = 18 h
    minutosHora = xtotal_minutos * 24
    print(int(xtotal_dias), " Dias", int(minutosHora), " horas", int(resto_minutos), " minutos")
    
    # convert Greg Date to Julian Date expressed by integer number
    gregtojulian(int(anoIni), int(mesIni), int(diaIni), int(xtotal_dias))

    # convert Julian Date to Greg Date
    today = datetime.date.today()
    juliantogreg(2457764, today.year, today.month, today.day)
    
    dataSaida = format(diaIni) + "/" + format(int(mesIni)) + "/" + format(anoIni) + " " + format(int(minutosHora)) + ":" + format(int(resto_minutos))
    print(dataSaida)
    


if __name__ == ("__main__"):
    change_date("01/03/2010 23:35", "+", 26)

