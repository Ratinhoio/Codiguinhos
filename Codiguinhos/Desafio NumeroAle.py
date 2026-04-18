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
    
# def Dado
# def Cronômetro
# def recemNascido():
limpar()
sinais = ["-", "+", "x", "÷"]
tempoPausado = 0
pontuação = 0
dado = ["TempoIli", "nada"]
def tempoIli():
    print("Tempo Ilimitado!")
rolada = "Por enquanto nada"
while True:
    if pontuação % 5 == 0 and pontuação > 0:
        rolada = random.choice(dado)
    print(f"Poderes ->", rolada)
    if rolada == "TempoIli":
        tempoIli()
    limpar()
    tempoPausado = time.time()
    num1 = random.randint(1, 3)
    num2 = random.randint(1, 3)
    sinal = random.choice(sinais)
    if sinal == "+":
        resultado = num1 + num2
    elif sinal == "-":
        if num1 < num2:
            num1, num2 = num2, num1
        resultado = num1 - num2
    elif sinal == "x":
        resultado = num1 * num2
    elif sinal == "÷":
        resultado = num1 // num2
    conta = f"{num1} {sinal} {num2}"
    inicio = time.time()
    resposta = input(f"Qual a resposta da equação {conta} > ")
    if rolada == "TempoIli":
        tempoPausado = time.time() - tempoPausado
    else:
        tempoPausado = 0
    tempo = time.time() - inicio - tempoPausado
    if tempo > 5:
        print("Tempo excedido")
        time.sleep(2)
        break
    if not resposta.isdigit():
        print("Só número ne cara")
        dormir(2)
        limpar()
        continue
    resposta = int(resposta)
    if resposta == resultado:
        limpar()
        pontuação += 1
        continue
    else:
        limpar()
        break
limpar()
os.system('color 0b')
print(f"Você acertou {pontuação} equações!")
print("gay")
dormir(1)
