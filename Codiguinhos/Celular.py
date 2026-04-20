# Criar um celular com aplicativos
import os, random, time, unicodedata, winsound
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
            print("Tu achou mesmo que tinha?")
            time.sleep(2)
            print("Deu preguiça de fazer")
            time.sleep(2)
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
def calculadora():
    print("Bem-vindo à calculadora!")
    dormir(2)
    limpar()
    while True:
        num1 = float(input("Digite o primeiro número: "))
        dormir(1)
        limpar()
        print("Escolha a operação:")
        dormir(1)
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        escolha = int(input("Digite o número da operação desejada: "))
        if escolha > 4 or escolha <= 0:
            limpar()
            print("Opção inválida. Por favor, escolha uma operação válida.")
            dormir(1)
        elif not escolha.isdigit:
            limpar()
            print("Burro!")
            dormir(1)
            continue
        dormir(1)
        limpar()
        num2 = float(input("Digite o segundo número: "))
        dormir(1)
        limpar()

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
                    




menu()
