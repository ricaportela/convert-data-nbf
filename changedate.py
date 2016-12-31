""" Calcute a new date from value of minutes 
name: Ricardo Portela da Silva
date: 31/12/2016
"""
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
    hours_minutes_conv = minutesTotal / 60
    i, d = divmod(hours_minutes_conv, 1) # separate integer from decimal places 
    resto_minutes = d * 60
    total_dias = hours_minutes_conv / 24
    i, d = divmod(total_dias, 1) #  separate integer from decimal places = 0.75 / 24
    xtotal_days = i
    xtotal_minutes = d
    minutes_hour = xtotal_minutes * 24
    print(int(xtotal_days), " Dias", int(minutes_hour), " horas", int(resto_minutes), " minutos")

    # convert Greg Date to Julian Date expressed by integer number
    g2jd = gregtojulian(int(yearIni), int(monthIni), int(dayIni), int(xtotal_days), op)

    # convert Julian Date to Greg Date
    today = datetime.date.today()
    yr, mo, dy = juliantogreg(g2jd, today.year, today.month, today.day)

    date_output = "%02d/%02d/%02d %02d:%02d" % (dy, mo, yr, minutes_hour, resto_minutes)
    print(date_output)

if __name__ == ("__main__"):
     change_date("01/01/2010 23:35", "+", 9000)


