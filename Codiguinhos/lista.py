# Primeiro
import os
import time
while True:
    os.system("cls")
# Segundo
    contadorDicas = 0
    totalErros = 0
# Terceiro
    desafiante = input("Nome do Desafiante: ")
    competidor = input("Nome do Competidor: ")
    os.system("cls")
# Quarto
    palavra = input("Palavra Chave: ")
    secreta = "*" * len(palavra)
    dica1 = input("Dica1: ")
    dica2 = input("Dica2: ")
    dica3 = input("Dica3: ")
# Quinto
    while True:
        os.system("cls")
        print(f"(1) Jogar")
        print(f"(2) Dica")
        print(f"A palavra secreta é: {secreta}")
        print(f"Total de erros: {totalErros}")
# Sexto
        opcao = input()
        if opcao == "1":
            tentativa = input("Informe a letra: ")
            posicao = 0
            acertou = False
            secreta = list(secreta)

            for letra in palavra:
                if letra == tentativa:
                    secreta[posicao] = letra
                    acertou = True
                posicao += 1
                
            secreta = "".join(secreta)
            if acertou == False:
                totalErros += 1
            
            if "*" not in secreta:
                print(f"O competidor {competidor} ganhou!")
                print(f"O desafiante {desafiante} perdeu!")
                time.sleep(2)
                break
            if totalErros == 6:
                print(f"O desafiante {desafiante} ganhou!")
                print(f"O competidor {competidor} perdeu!")
                time.sleep(2)
                break
        elif opcao == "2":
            contadorDicas += 1
            if contadorDicas == 1:
                print(f"Dica 1: {dica1}")
                time.sleep(2)
            elif contadorDicas == 2:
                print(f"Dica 2: {dica2}")
                time.sleep(2)
            elif contadorDicas == 3:
                print(f"Dica 3: {dica3}")
                time.sleep(2)
        else:
            print("Opção inválida!")
            time.sleep(2)




            
                
                
                
                
                
                
                
                
                
