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
    limpar()
    num1 = input("Digite o primeiro número: ")
    if not num1.replace('.', '', 1).replace('-', '', 1).isdigit():
        limpar()
        print("Burro!")
        dormir(1)
        limpar()
        continue
    limpar()
    num1 = float(num1)
    print("Operações disponíveis: +  -  *  x  /  √")
    escolha = input("Digite a operação desejada: ")
    if escolha not in ["+", "-", "*", "/", "√"]:
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
        else:
            print(f"Resultado: {math.sqrt(num1)}")
            input("ENTER...")
            continue             
    limpar()
    num2 = input("Digite o segundo número: ")
    if not num2.replace('.', '', 1).replace('-', '', 1).isdigit():
        limpar()
        print("Burro!")
        dormir(1)
        limpar()
        continue
    num2 = float(num2)
    dormir(0.5)
    limpar()
    if escolha == "+":
        print(f"O resultado da adição é: {num1 + num2}")
        dormir(1)
    elif escolha == "-":
        print(f"O resultado da subtração é: {num1 - num2}")
        dormir(1)
    elif escolha == "*":
        print(f"O resultado da multiplicação é: {num1 * num2}")
        dormir(1)
    elif escolha == "/":
        if num2 == 0:
            print("Erro: Divisão por zero não é permitida!")
        else:
            print(f"O resultado da divisão é: {num1 / num2}")
    input("ENTER...")