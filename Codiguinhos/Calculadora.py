import os, random, time, math 
def dormir(segundos):
    time.sleep(segundos)
def limpar():
    os.system('cls')
limpar()
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
    escolha = input("Digite a operação desejada: ")
    if escolha not in ["+", "-", "*", "x", "/", "√"]:
                limpar()
                print("Opção inválida. Por favor, escolha uma operação válida.")
                dormir(1)
                limpar()
                continue
    if escolha == "√":
            if num1 < 0:
                print("Não existe raiz de número negativo!")
                dormir(2)
                continue
            else
            print(f"Resultado: {math.sqrt(num1)}")
            input("ENTER...")
            continue
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

if escolha in ["+", "-", "*", "x", "/", "√"]:
    if escolha == "+":
        resultado = num1 + num2
        print(f"O resultado da adição é: {resultado}")
        dormir(1)
    elif escolha == "-":
        resultado = num1 - num2
        print(f"O resultado da subtração é: {resultado}")
        dormir(1)
    elif escolha == "*" or escolha == "x":
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



