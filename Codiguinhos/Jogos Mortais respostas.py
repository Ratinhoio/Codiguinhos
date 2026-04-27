# Henrique Zonta Tramontina  RA: 1139226
import os, time, random
while True:
    os.system('cls')
    os.system('color 0d')
    print("1 - Começar a tortura...")
    print("2 - Sair")
    escolha = input("> ")
    if escolha == "2":
        os.system('cls')
        exit()
    if escolha != "1":
        os.system('cls')
        print("Só tem duas opções caraKKKKKKK")
        input("Aperte Enter para voltar")
        continue
    os.system('cls')  # Limpar o terminal
    os.system('color 0a')  # Mudar o terminal para verde
    print("Bem-vindo. Você está prestes a enfrentar o maior desafio da sua vida...")
    time.sleep(2.5)  # Pausar por 3 segundos
    os.system('cls')  # Limpar o terminal
    os.system('color 0c')  # Mudar o terminal para vermelho
    print("Fase 1: Jogo de azar")
    numero = random.randint(1, 3)
    time.sleep(2)
    os.system('cls')
    print("Aguarde.")
    time.sleep(0.5)
    os.system('cls')
    print("Aguarde..")
    time.sleep(0.5)
    os.system('cls')
    print("Aguarde...")
    time.sleep(0.5)
    os.system('cls')
    print(numero)
    chute = int(input("Digite seu chute (1, 2 ou 3): "))
    if chute == numero:
        print("Você acertou!")
    else:
        os.system('cls')
        print("Meus Deus que azarado!")
        print("Você perdeu pra um número de 1 a 3. Reflita...")
        time.sleep(0.5)
        input("Aperte Enter para sair")
        os.system('cls')
        continue
        # Se o usuário errar, o sistema deve avacalhar chamando ele de azarado e apresentar a mensagem da morte (bem criativa kkk) encerrar o jogo com o comando quit().
    time.sleep(1.5)
    os.system('cls')
    print("Fase 2: Potência mortal")
    time.sleep(1.5)
    os.system('cls')
    print("Aguarde.")
    time.sleep(0.5)
    os.system('cls')
    print("Aguarde..")
    time.sleep(0.5)
    os.system('cls')
    print("Aguarde...")
    time.sleep(0.5)
    os.system('cls')
    numero2 = random.randint(1, 10)
    numero3 = random.randint(1, 3)
    calculo = numero2 ** numero3
    print(calculo)
    resposta =int(input(f"Qual é o resultado da operação {numero2} ^ {numero3}: "))
    if resposta == numero2 ** numero3:
        print("Você acertou! Próxima fase...")
    else:
        os.system('cls')
        print("Matemática básica te derrotou.")
        time.sleep(0.5)
        input("Aperte Enter para voltar")
        os.system('cls')
        continue
    time.sleep(1.5)
    os.system('cls')
    print("Fase 3: Fórmula do desespero")
    time.sleep(1.5)
    os.system('cls')
    print("Aguarde.")
    time.sleep(0.5)
    os.system('cls')
    print("Aguarde..")
    time.sleep(0.5)
    os.system('cls')
    print("Aguarde...")
    time.sleep(0.5)
    os.system('cls')
    print("FAÇA AGORA!")
    calculo = (chute + resposta) ** chute - resposta
    print(calculo)
    resposta2 = int(input("(respostaFase1 + respostaFase2) ^ respostaFase1 - respostaFase2: "))
    if resposta2 == (chute + resposta) ** chute - resposta:
        print("Vivo, por enquanto...")
    else:
        print("Entrou em pânico?")
        time.sleep(0.5)
        input("Aperte Enter para voltar")
        continue
    time.sleep(1.5)
    os.system('cls')
    print("Fase 4: Jogo da Memória Mortal")
    time.sleep(1.5)
    os.system('cls')
    print("Aguarde.")
    time.sleep(0.5)
    os.system('cls')
    print("Aguarde..")
    time.sleep(0.5)
    os.system('cls')
    print("Aguarde...")
    time.sleep(0.5)
    os.system('cls')
    os.system('color 01') # Mudar o terminal para azul
    print("Memorize a sequência de números que aparecerá na tela. Você terá 2 segundos para memorizar cada número.")
    input("Aperte Enter para iniciar ")
    os.system('cls')
    sequencia1 = random.randint(1, 5)
    sequencia2 = random.randint(1, 5)
    sequencia3 = random.randint(1, 5)
    sequencia4 = random.randint(1, 5)
    sequencia5 = random.randint(1, 5)
    os.system('color 0c') # Mudar o terminal para vermelho
    print(sequencia1)
    time.sleep(2)
    os.system('cls')
    os.system('color 0a') # Mudar o terminal para verde
    print(sequencia2)
    time.sleep(2)
    os.system('cls')
    os.system('color 0c') # Mudar o terminal para vermelho
    print(sequencia3)
    time.sleep(2)
    os.system('cls')
    os.system('color 0a') # Mudar o terminal para verde
    print(sequencia4)
    time.sleep(2)
    os.system('cls')
    os.system('color 0c') # Mudar o terminal para vermelho
    print(sequencia5)
    time.sleep(2)
    os.system('cls')
    os.system('color 0a') # Mudar o terminal para verde
    print(sequencia1, sequencia2, sequencia3, sequencia4, sequencia5)
    rsequencia1 = int(input("Digite o primeiro número da sequência: "))
    os.system('cls')
    print(sequencia2, sequencia3, sequencia4, sequencia5)
    rsequencia2 = int(input("Digite o segundo número da sequência: "))
    os.system('cls')
    print(sequencia3, sequencia4, sequencia5)
    rsequencia3 = int(input("Digite o terceiro número da sequência: "))
    os.system('cls')
    print(sequencia4, sequencia5)
    rsequencia4 = int(input("Digite o quarto número da sequência: "))
    os.system('cls')
    print(sequencia5)
    rsequencia5 = int(input("Digite o quinto número da sequência: "))
    os.system('cls')
    if rsequencia1 == sequencia1 and rsequencia2 == sequencia2 and rsequencia3 == sequencia3 and rsequencia4 == sequencia4 and rsequencia5 == sequencia5:
        print("Parabéns, última fase! Você conseguiu sobreviver a todos os desafios, mas o mais difícil ainda está por vir...")
    else:
        print("Peixinho dourado ")
        time.sleep(0.5)
        input("Aperte Enter para voltar")
        continue
    time.sleep(1.5)
    os.system('cls')
    os.system('color 0c') # Mudar o terminal para vermelho
    print("Fase 5: O Enigma Final")
    print("Um programador encontra um nano computador que trabalha apenas com bits. O computador tem exatamente 41.943.040 bits de memória. Quantos Megabytes isso representa?")
    print("(Lembre-se que 1 byte = 8 bits, 1024 bytes = 1 KB, 1024 KB = 1 MB.)")
    resposta3 = float(input("Digite sua resposta em MB: "))
    if resposta3 == 5 or resposta3 == 5.0:
        os.system('cls')
        print("Parabéns, você venceu o jogo! Você é um verdadeiro sobrevivente dos jogos mortais!")
        input("Aperte Enter para sair")
        continue
    else:
        os.system('cls')
        print("Que decepção.")
        time.sleep(1.5)
        os.system('cls')
        print("Que decepção..")
        time.sleep(1.5)
        os.system('cls')
        print("Que decepção...")
        time.sleep(1.5)
        input("Aperte Enter para voltar")
        os.system('cls')
        continue