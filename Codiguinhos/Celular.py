# Criar um celular com aplicativos
import os, random, time, unicodedata, winsound, calendar
from datetime import datetime
# Funções:
def limpar():
    os.system('cls')
def aguarde():
    for i in ["Aguarde.", "Aguarde..", "Aguarde..."]:
        print(i)
        dormir(0.8)
        limpar()
def carregando():
    for i in ["Carregando.", "Carregando..", "Carregando..."]:
        print(i)
        dormir(0.8)
        limpar()
def dormir(segundos):
    time.sleep(segundos)
def menu():
    while True:
        limpar()
        os.system('color 0b')
        print("1 - Calculadora")
        print("2 - Calendário")
        print("3 - Sair :(")
        opcao = input("O que quer fazer? > ")
        if opcao == "1":
            limpar()
            calculadora()
            break
        elif opcao == "2":
            limpar()
            calendario()
            break
        elif opcao == "3":
            limpar()
            print("Tiau :(")
            time.sleep(2)
            limpar()
            exit()
        elif not opcao.isdigit():
            limpar()
            print("Só pode número ne burrão")
            time.sleep(2)
        else:
            limpar()
            print("mano, só tem 3 opções \nE tu ainda consegue errar!")
            time.sleep(2)
# Calculadora
def calculadora():
    print("Bem-vindo à calculadora!")
    dormir(2)
    limpar()
    while True:
        num1 = input("Digite o primeiro número: ")
        if not num1.isdigit():
            limpar()
            print("Burro!")
            dormir(1)
            limpar()
            continue
        dormir(1)
        limpar()
        num1 = float(num1)
        
        print("Escolha a operação:")
        dormir(0.5)
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        
        escolha = int(input("Digite o número da operação desejada: "))
        
        if not escolha.isdigit():
            limpar()
            print("Burro!")
            dormir(1)
            limpar()
            continue
        if escolha not in [1, 2, 3, 4]:
            limpar()
            print("Opção inválida. Por favor, escolha uma operação válida.")
            dormir(1)
        dormir(1)
        limpar()
        num2 = input("Digite o segundo número: ")
        if not num2.isdigit():
            limpar()
            print("Burro!")
            dormir(1)
            limpar()
            continue
        dormir(1)
        limpar()
        break
    num2 = float(num2)

    if escolha in [1, 2, 3, 4]:
        if escolha == 1:
                resultado = num1 + num2
                print(f"O resultado da adição é: {resultado}")
        elif escolha == 2:
                resultado = num1 - num2
                print(f"O resultado da subtração é: {resultado}")
        elif escolha == 3:
                resultado = num1 * num2
                print(f"O resultado da multiplicação é: {resultado}")
        elif escolha == 4:
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"O resultado da divisão é: {resultado}")
                else:
                    print("Erro: Divisão por zero não é permitida.")
# Calendário
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
def calendario():
    agora = hoje()
    limpar()
    while True:
        limpar()
        print(f"{agora.strftime("%d/%m/%Y")}")
        os.system('color 0A')
        ano = int(input("Digite o ano: "))
        mes = int(input("Digite o mês (0-12): "))
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
menu()
