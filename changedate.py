""" Calcular Data a partir de uma quantidade de minutos """
MINUTOSENTRADA = 4000
OPERADOR = "+"
DATA_E, HORA_E = "31/12/2016 23:35".split(" ", 2)
DIA_E, MES_E, ANO_E = DATA_E.split("/", 3)
HR_E, MINU_E = HORA_E.split(":", 2)

# transformar tudo em minutos
# converter horas em minutos

MIN_TOT_E = (int(HR_E) * 60) + int(MINU_E) + MINUTOSENTRADA
print("Total de Minutos ", MIN_TOT_E)

# 5415 / 60 minutos = 90.25 = .25 * 60
TOTAL_HORAS = MIN_TOT_E / 60

# 90h e 15 mine
I, D = divmod(TOTAL_HORAS, 1)
TOTAL_MINUTOS = D * 60

# 90h / 24h = 3.75 3 dias
TOTAL_DIAS = TOTAL_HORAS / 24

I, D = divmod(TOTAL_DIAS, 1)

# 3d 3.75 (0.75 * 24)  = 18 h
TOTAL_HORAS2 = D * 24

print(int(I), " Dias", int(TOTAL_HORAS2), " horas", int(TOTAL_MINUTOS), " minutos")


# 3d 18h e 15min
# 4000 min / 60 min =  No. de horas 66.66
# 66h e 40 min ... peguei a dízima e multipliquei por 66*60
# Então fica assim...
# 66 h / 24 h = No. de dias
# Agora pego o número de dias
# 2d 2.75 (dizima 0.75 * 24)
# 0,75 * 24 = 18 h
# 2D 18H 40M

