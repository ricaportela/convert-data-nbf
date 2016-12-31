def gregtojulian (yr, mo, dy, qty_of_days, op):
    """ Receive the date from parameter """
    juliandays = 0
    a = int((14-mo)/12)
    y = yr + 4800 - a
    m = mo + 12*a - 3
    g2jd = dy + int((153*m+2)/5)+365*y+int(y/4)-int(y/100)+int(y/400)-32045
    if op == '+':
        g2jd = g2jd + qty_of_days
    else:
        g2jd = g2jd - qty_of_days
    print("Greg to Julian: ", g2jd)
    juliandays = g2jd
    return juliandays



