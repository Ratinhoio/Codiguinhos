import calendar
ano = int(input("Digite o ano: "))
mes = int(input("Digite o mês (1-12): "))
dia = int(input("Digite o dia: "))
if mes == 0:
    print(calendar.calendar(ano))
else:
    print(calendar.month(ano, mes, dia))
