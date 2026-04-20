import calendar, os, time
from datetime import datetime
def limpar():
    os.system('cls')
def pintado(ano, mes, dia):
    cal = calendar.month(ano, mes)
    linhas = cal.split("\n")
    verde = "\033[92m"
    reset = "\033[0m"
    calendario = []
    for linha in linhas:
        linha = linha.replace(f" {dia:2} ", f" {verde}{dia:2}{reset} ")

        calendario.append(linha)   
    return "\n".join(calendario)
def hoje():
    return datetime.now()
agora = hoje()
limpar()
print(f"{agora.strftime("%d/%m/%Y")}")
time.sleep(5)
while True:
    limpar()
    os.system('color 0A')
    ano = int(input("Digite o ano: "))
    mes = int(input("Digite o mês (1-12): "))
    if mes < 0 or mes > 12:
        limpar()
        os.system('color 4')
        print("Mês inválido!")
        time.sleep(2)
        continue
    if mes == 0:
        limpar()
        print(calendar.calendar(ano))
        exit()
    dia = int(input("Digite o dia: "))
    try:
        data = datetime(ano, mes, dia)
        break
    except ValueError:
        limpar()
        os.system('color 4')
        print("Dia inválido!")
        time.sleep(2)
        continue
limpar()
print(pintado(ano, mes, dia))
indice = data.weekday()
dias = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
print(f"\n{dia}/{mes}/{ano} é {dias[indice]}")
time.sleep(2)