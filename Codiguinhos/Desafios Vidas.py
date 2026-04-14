import os, random, time
vidas = 3
os.system('cls')
while vidas > 0:
    resposta1 = input("Quantas letras tem no alfabeto? ")
    if not resposta1.isdigit():
            os.system('cls')
            print("Digite apenas números!\n")
            continue  # volta pro começo sem perder vida
    if resposta1 != "26":
            os.system('cls')
            print("Errou, perdeu uma vida!")
            vidas -= 1
            print(f"Você tem {vidas} vidas")
    else: 
        os.system('cls')
        print("Parabéns")
        print(f"Você tem {vidas} vidas")
        time.sleep(1.5)
        os.system('cls')
        print("Carregando...")
        time.sleep(1.5)
        os.system('cls')
        break
while vidas > 0:
    resposta2 = input("Em que ano estamos? ")
    if not resposta2.isdigit():
        os.system('cls')
        print("Digite apenas números!\n")
        continue  # volta pro começo sem perder vida
    if resposta2 != "2026":
        os.system('cls')
        print("Errou, perdeu uma vida!")
        vidas -= 1
        print(f"Você tem {vidas} vidas")
    else: 
        os.system('cls')
        print("Parabéns")
        print(f"Você tem {vidas} vidas")
        time.sleep(1.5)
        os.system('cls')
        print("Carregando...")
        time.sleep(1.5)
        os.system('cls')
        break
os.system('cls')
os.system('color 0c')
print("Acabou suas vidas... Fim de jogo!")
