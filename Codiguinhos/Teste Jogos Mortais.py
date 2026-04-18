# Importar bibliotecas
import os, time, random

# Criar função de limpar
def limpar():
    os.system('cls')
    
# Criar função de aguarde
def aguarde():
    for i in ["Aguarde.", "Aguarde..", "Aguarde..."]:
        print(i)
        time.sleep(0.8)
        limpar()

# Criar função para fim de jogo
def game_over():
    limpar()
    print("💀 VOCÊ ERROU! 💀")
    print("Reiniciando o jogo...")
    time.sleep(2)
    limpar()


def fase1(): 
    limpar() # Limpar o terminal
    os.system('color 0a')  # Mudar o terminal para verde
    print("Bem-vindo. Você está prestes a enfrentar o maior desafio da sua vida...")
    time.sleep(3)  # Pausar por 3 segundos
    limpar()  # Limpar o terminal
    os.system('color 0c')  # Mudar o terminal para vermelho
    print("Fase 1: Jogo de azar")
    numero = random.randint(1, 3)
    time.sleep(2)
    limpar()
    aguarde()
    
    print(numero)
    try:
        chute = int(input("Digite seu chute (1, 2 ou 3): "))
    except: chute!= numero
    game_over()
    return False
   
def fase2():
    print("Fase 2: Potência mortal")
    time.sleep(2)
    limpar()
    aguarde()
    numero2 = random.randint(1, 10)
    numero3 = random.randint(1, 3)
    calculo = numero2 ** numero3
    print(calculo)
    resposta =int(input(f"Qual é o resultado da operação {numero2} ** {numero3}: "))
    if resposta == numero2 ** numero3:
        print("Você acertou! Próxima fase...")
    else:
        print("Você errou!")
        exit()
    time.sleep(2)
    limpar()
def fase3():
    print("Fase 3: Fórmula do desespero")
    time.sleep(2)
    limpar()
    aguarde()
    print("FAÇA AGORA!")
    calculo = (chute + resposta) ** chute - resposta
    print(calculo)
    resposta2 = int(input("(respostaFase1 + respostaFase2) ** respostaFase1 - respostaFase2: "))
    if resposta2 == (chute + resposta) ** chute - resposta:
        print("Vivo, por enquanto...")
    else:
        print("Você errou!")
        exit()
    time.sleep(2)
    limpar()
    print("Fase 4: Jogo da Memória Mortal")
    time.sleep(2)
    limpar()
    aguarde()
    os.system('color 01') # Mudar o terminal para azul
    print("Memorize a sequência de números que aparecerá na tela. Você terá 2 segundos para memorizar cada número.")
    time.sleep(5)
    limpar()
    sequencia1 = random.randint(1, 5)
    sequencia2 = random.randint(1, 5)
    sequencia3 = random.randint(1, 5)
    sequencia4 = random.randint(1, 5)
    sequencia5 = random.randint(1, 5)
    os.system('color 0c') # Mudar o terminal para vermelho
    print(sequencia1)
    time.sleep(2)
    limpar()
    os.system('color 0a') # Mudar o terminal para verde
    print(sequencia2)
    time.sleep(2)
    limpar()
    os.system('color 0c') # Mudar o terminal para vermelho
    print(sequencia3)
    time.sleep(2)
    limpar()
    os.system('color 0a') # Mudar o terminal para verde
    print(sequencia4)
    time.sleep(2)
    limpar()
    os.system('color 0c') # Mudar o terminal para vermelho
    print(sequencia5)
    time.sleep(2)
    limpar()
    os.system('color 0a') # Mudar o terminal para verde
    print(sequencia1, sequencia2, sequencia3, sequencia4, sequencia5)
    rsequencia1 = int(input("Digite o primeiro número da sequência: "))
    limpar()
    print(sequencia2, sequencia3, sequencia4, sequencia5)
    rsequencia2 = int(input("Digite o segundo número da sequência: "))
    limpar
    print(sequencia3, sequencia4, sequencia5)
    rsequencia3 = int(input("Digite o terceiro número da sequência: "))
    limpar()
    print(sequencia4, sequencia5)
    rsequencia4 = int(input("Digite o quarto número da sequência: "))
    limpar()
    print(sequencia5)
    rsequencia5 = int(input("Digite o quinto número da sequência: "))
    limpar()
    if rsequencia1 == sequencia1 and rsequencia2 == sequencia2 and rsequencia3 == sequencia3 and rsequencia4 == sequencia4 and rsequencia5 == sequencia5:
        print("Parabéns, última fase! Você conseguiu sobreviver a todos os desafios, mas o mais difícil ainda está por vir...")
    else:
        print("Você errou!")
        exit()
    time.sleep(2)
    limpar()
    os.system('color 0c') # Mudar o terminal para vermelho
    print("Fase 5: O Enigma Final")
    print("Um programador encontra um nano computador que trabalha apenas com bits. O computador tem exatamente 41.943.040 bits de memória. Quantos Megabytes isso representa?")
    print("(Lembre-se que 1 byte = 8 bits, 1024 bytes = 1 KB, 1024 KB = 1 MB.)")
    resposta3 = float(input("Digite sua resposta em MB: "))
    if resposta3 == 5:
        limpar
        print("Parabéns, você venceu o jogo! Você é um verdadeiro sobrevivente dos jogos mortais!")
    else:
        limpar()
        print("Que decepção.")
        time.sleep(1.5)
        limpar
        print("Que decepção..")
        time.sleep(1.5)
        limpar
        print("Que decepção...")
        time.sleep(1.5)
        limpar
        exit()
while True:
    limpar()

    chute = fase1()
    if not chute:
        continue

    resposta2 = fase2()
    if not resposta2:
        continue

    if not fase3(chute, resposta2):
        continue

    if not fase4():
        continue

    if not fase5():
        continue
    else:
        break
    