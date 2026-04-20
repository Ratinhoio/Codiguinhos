import calendar, os, time, datetime
os.system('cls')
os.system('color 0A')
ano = int(input("Digite o ano: "))
mes = int(input("Digite o mês (1-12): "))
dia = int(input("Digite o dia: "))
if mes == 0:
    os.system('cls')
    print(calendar.calendar(ano))
elif mes <= 12:
    os.system('cls')
    print(calendar.month(ano, mes))
    indice = calendar.weekday(ano, mes, dia)
    dias = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
    print(f"{dia}/{mes}/{ano} é {dias[indice]}")
else:
    os.system('cls')
    os.system('color 4')
    print("Data inválida!")
    time.sleep(2)