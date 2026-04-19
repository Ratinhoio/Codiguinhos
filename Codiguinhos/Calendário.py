import calendar, os
ano = int(input("Digite o ano: "))
mes = int(input("Digite o mês (1-12): "))
if mes == 0:
    os.system('cls')
    print(calendar.calendar(ano))
else:
    os.system('cls')
    print(calendar.month(ano, mes))