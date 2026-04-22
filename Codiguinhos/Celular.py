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
        elif opcao == "2":
            limpar()
            calendario()
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
        if not num1.replace('.', '', 1).isdigit():
            limpar()
            print("Burro!")
            dormir(1)
            limpar()
            continue
        dormir(0.5)
        limpar()
        num1 = float(num1)
        dormir(0.5)
        while True:
            escolha = input("Digite a operação desejada: ")
            if escolha not in ["+", "-", "*", "/"]:
                limpar()
                print("Opção inválida. Por favor, escolha uma operação válida.")
                dormir(1)
                limpar()
                continue
            break
        dormir(0.5)
        limpar()
        num2 = input("Digite o segundo número: ")
        if not num2.replace('.', '', 1).isdigit():
            limpar()
            print("Burro!")
            dormir(1)
            limpar()
            continue
        dormir(0.5)
        limpar()
        break
    num2 = float(num2)

    if escolha in ["+", "-", "*", "/"]:
        if escolha == "+":
                resultado = num1 + num2
                print(f"O resultado da adição é: {resultado}")
                dormir(1)
        elif escolha == "-":
                resultado = num1 - num2
                print(f"O resultado da subtração é: {resultado}")
                dormir(1)
        elif escolha == "*":
                resultado = num1 * num2
                print(f"O resultado da multiplicação é: {resultado}")
                dormir(1)
        elif escolha == "/":
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"O resultado da divisão é: {resultado}")
                    dormir(1)
                else:
                    print("Erro: Divisão por zero não é permitida.")
    input("Pressione ENTER para continuar...")
    while True:               
        limpar()
        os.system('color 0b')
        print("1 - Calculadora")
        print("2 - Menu")
        print("3 - Sair")
        opcao = input("O que quer fazer? > ")
        if opcao == "1":
            limpar()
            calculadora()
            break
        elif opcao == "2":
            limpar()
            menu()
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
            print("mano, só tem 2 opções \nE tu ainda consegue errar!")
            time.sleep(2)
        
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
        print(f"{agora.strftime('%d/%m/%Y')}")
        os.system('color 0A')
        ano = input("Digite o ano: ")
        if not ano.isdigit():
            limpar()
            print("Apenas números!")
            dormir(1)
            continue
        ano = int(ano)
        mes = input("Digite o mês (0-12): ")
        if not mes.isdigit():
            limpar()
            print("Apenas números!")
            dormir(1)
            continue
        mes = int(mes)
        if mes < 0 or mes > 12:
            limpar()
            os.system('color 4')
            print("Mês inválido!")
            dormir(2)
            continue
        if mes == 0:
            limpar()
            print(calendar.calendar(ano))
            return
        dia = input("Digite o dia: ")
        if not dia.isdigit():
            limpar()
            print("Apenas números!")
            dormir(1)
            continue
        dia = int(dia)
        try:
            data = datetime(ano, mes, dia)
            break
        except ValueError:
            limpar()
            os.system('color 4')
            print("Dia inválido!")
            dormir(2)
            continue
    limpar()
    print(pintado(ano, mes, dia))
    indice = data.weekday()
    dias = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]
    print(f"\n{dia}/{mes}/{ano} é {dias[indice]}")
    input("Pressione ENTER para continuar...")
menu()
