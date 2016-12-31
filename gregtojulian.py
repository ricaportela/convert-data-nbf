def gregtojulian (yr, mo, dy, qty_of_days, op):
    """ Receive the date from parameter 
    name: Ricardo Portela da Silva
    date: 31/12/2016
    """
    juliandays = 0
    a = int((14-mo)/12)
    y = yr + 4800 - a
    m = mo + 12*a - 3
    g2jd = dy + int((153*m+2)/5)+365*y+int(y/4)-int(y/100)+int(y/400)-32045
    if op == '+':
        g2jd = g2jd + qty_of_days
    else:
        g2jd = g2jd - qty_of_days
    return g2jd



