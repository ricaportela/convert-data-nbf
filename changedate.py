""" Calcute a new date from value of minutes """
from gregtojulian import gregtojulian
from juliantogreg import juliantogreg
import datetime
import sys

def change_date(date, op, value):
    """ calculate new date """
    dateEnt, hourEnt = date.split(" ", 2)
    dayIni, monthIni, yearIni = dateEnt.split("/", 3)
    hourIni, minuIni = hourEnt.split(":", 2)
    # convert all to minutes
    # convert hours in minutes to adding in total minutes
    minutesTotal = (int(hourIni) * 60) + int(minuIni) + value
    # print("Total de Minutos: ", minutesTotal)
    # 5415 / 60 minutos = 90.25 => separate integer from decimal places 0.25 * 60  = 15
    hours_minutes_conv = minutesTotal / 60
    # 90h e 15 min - i = integer part and d = decimal part
    i, d = divmod(hours_minutes_conv, 1)
    resto_minutos = d * 60
    # 90h / 24h = 3.75 => separate integer from decimal places = 0.75 / 24
    total_dias = hours_minutes_conv / 24
    i, d = divmod(total_dias, 1)
    xtotal_days = i
    xtotal_minutes = d
    # 3d 3.75 (0.75 * 24)  = 18 h
    minutesHour = xtotal_minutes * 24
    print(int(xtotal_days), " Dias", int(minutesHour), " horas", int(resto_minutos), " minutos")

    # convert Greg Date to Julian Date expressed by integer number
    g2jd = gregtojulian(int(yearIni), int(monthIni), int(dayIni), int(xtotal_days), op)

    # convert Julian Date to Greg Date
    today = datetime.date.today()
    yr, mo, dy = juliantogreg(g2jd, today.year, today.month, today.day)

    dateOutput = format(int(dy)) + "/" + format(int(mo)) + "/" + format(int(yr)) + " " + format(int(minutesHour)) + ":" + format(int(resto_minutos))
    print(dateOutput)
    

if __name__ == ("__main__"):
     change_date("01/01/2010 23:35", "+", 4000)
#    change_date(sys.argv[1], sys.argv[2], sys.argv[3])

