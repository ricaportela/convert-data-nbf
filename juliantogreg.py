def juliantogreg (jd, yr, mo, dy):
    a = jd + 32044
    b = int((4*a+3)/146097)
    c = a - int((146097*b)/4)
    d = int((4*c+3)/1461)
    e = c - int(1461*d/4)
    m = int((5*e+2)/153)
    dy = e - int((153*m+2)/5) + 1
    mo = m + 3 - 12*int(m/10)
    yr = 100*b + d - 4800 + int(m/10)
    print(yr, "/", mo, "/", dy)


