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
            limpar()
            print("1 - Recém-nascido")
            print("2 - Normal")
            print("3 - Macho Alpha")
            opcao2 = input("Qaul dificuldade deseja? > ")
            if opcao2 == "1":
                break
            # Criar outras dificuldades
        elif opcao == "2":
            limpar()
            print("Sei la por enquanto")
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
menu()
print("gay")
def recemNascido():
    limpar()
    os.system('color0a')
    print("Bem-vindo ao Desafio Aleatório")
    
    