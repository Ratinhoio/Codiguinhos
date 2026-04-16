import os, random, time, unicodedata, winsound # Importar bibliotecas
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
def hud(vidas):
    texto = "vida" if vidas == 1 else "vidas"
    aviso = "FUDEU, ÚLTIMA VIDA!"
    tempo = time.time() - inicio - tempoPausado
    print(f"❤️  Vidas: {vidas} {texto}") 
    if vidas == 1:
        print(aviso)
    print(f"⏳ Tempo: {tempo:.1f}s")
    print("=" * 30)
def tela(vidas, msg=""):
    limpar()
    hud(vidas)
    if msg:
        print(msg)
def removerAcento(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn')
def dormir(segundos):
    global tempoPausado
    inicioPausa = time.time()
    time.sleep(segundos)
    tempoPausado += time.time() - inicioPausa
def menu():    
    while True:
        limpar()
        os.system('color 0b')
        print("1 - Jogar")
        print("2 - Instruções (para burros)")
        print("3 - Sair :(")
        opcao = input("O que quer fazer? > ")
        if opcao == "1":
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
def jogo():
    global tempoPausado, inicio
    vidas = 3
    elogios = ["bonito", "lindo", "genio", "perfeito", "cheiroso", "atraente", "sexy", "maravilhoso", "brabo", "inteligente", "gostoso", "esbelto", "calmo", "incrivel", "amoroso", "fofo", "carinhoso", "safado", "gentil", "alegre", "engraçado", "atencioso", "parceiro", "esforçado"]
    xingamentos = ["chato", "birrento", "lerdo", "ciumento", "teimoso", "desastrado", "burro"]
    limpar()
    os.system('color 0a')
    print("Bem-vindo ao Desafio Ridículo")
    time.sleep(1.5)
    limpar()
    tempoPausado = 0
    inicio = time.time()
    aguarde()
    while vidas > 0:
        tela(vidas)
        resposta1 = input("Quantas letras tem no alfabeto? ")
        if not resposta1.isdigit():
            tela(vidas, "Digite apenas números!\n")
            dormir(1.5)
            continue  # volta pro começo sem perder vida
        if resposta1 != "26":
            vidas -= 1
            tela(vidas, "ERROU!")
            dormir(1.5)
        else: 
            tela(vidas, "Parabéns, próxima pergunta!")
            dormir(1)
            break
    while vidas > 0:
        tela(vidas)
        resposta2 = input("Em que ano estamos? ")
        if not resposta2.isdigit():
            tela(vidas, "Digite apenas números!\n")
            dormir(1.5)
            continue  # volta pro começo sem perder vida
        if resposta2 != "2026":
            vidas -= 1
            tela(vidas, "ERROU!")
            dormir(1.5)
        else: 
            tela(vidas, "Parabéns, próxima pergunta!")
            dormir(1)
            break
    while vidas > 0:
        tela(vidas)
        resposta3 = input("Quantos lados tem um cubo? ")
        if not resposta3.isdigit():
            tela(vidas, "Digite apenas números!\n")
            dormir(1.5)
            continue  # volta pro começo sem perder vida
        if resposta3 != "6":
            vidas -= 1
            tela(vidas, "ERROU!")
            dormir(1.5)
        else: 
            tela(vidas, "Parabéns, próxima pergunta!")
            dormir(1)
            break
    while vidas > 0:
        tela(vidas)
        resposta4 = input("O que o criador do jogo é? ")
        resposta4 = removerAcento(resposta4.lower())
        if not (resposta4.isalpha() and resposta4.islower()):
            tela(vidas, "Palavra inválida! Digite apenas uma palavra\n")
            dormir(1.5)
            
            continue  # volta pro começo sem perder vida
        if resposta4 in elogios:
            tela(vidas, "Ownnnnnnnn que fofinho, continue assim!")
            break
        elif resposta4 == "gay":
            vidas -= 1
            limpar()
            print("Gay? Sério? Se mata vei")
            dormir(1.5)
            print("Perdeu uma vida por causa disso")
            dormir(1.5)
            continue
        elif resposta4 == "viado":
            vidas -= 1
            limpar()
            print("Que criatividade hein")
            dormir(1.5)
            print("Perdeu uma vida por causa disso")
            dormir(1.5)
            continue
        elif resposta4 in xingamentos:
            vidas = max(0, vidas, -3)
            limpar()
            print("???????????????????????\nQual o seu problema?")
            dormir(2)
        else: 
            vidas -= 1
            tela(vidas, "Não gostei, melhore...")
            dormir(1)
        
    tempo = time.time() - inicio - tempoPausado
    dormir(1.5)
    limpar()
    aguarde()
    limpar()


    if vidas <= 0:
        os.system('color 0c')
        print("Acabaram suas vidas... Fim de jogo!")
        
    elif tempo > 15:
        os.system('color 0c')
        print("Seu tempo excediu o limite... Fim de jogo!")

    else:
        os.system('color 0b')
        print("GANHOUUUUUU!!!")

    print(f"Seu tempo final foi de {tempo:.1f}s")
    dormir(3)
    limpar()
menu()
jogo()