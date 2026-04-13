# Limpar o terminal e mudar o terminal para verde
import os, time, random
os.system('cls')  # Limpar o terminal
os.system('color 0a')  # Mudar o terminal para verde
print("Bem-vindo. Você está prestes a enfrentar o maior desafio da sua vida...")
time.sleep(3)  # Pausar por 3 segundos
os.system('cls')  # Limpar o terminal
os.system('color 0c')  # Mudar o terminal para vermelho

print("Fase 1: Jogo de azar")
numero = random.randint(1, 3)
print(numero)
chute = int(input("Digite seu chute (1, 2 ou 3): "))
if chute == numero:
    print("Você acertou!")
else:
    print("Você errou!")
    exit()
    # Se o usuário errar, o sistema deve avacalhar chamando ele de azarado e apresentar a mensagem da morte (bem criativa kkk) encerrar o jogo com o comando quit().
time.sleep(2)
os.system('cls')
print("Fase 2: Potência mortal")
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
os.system('cls')
print("Fase 3: Fórmula do desespero")
time.sleep(2)
os.system('cls')
print("Aguarde.")
time.sleep(0.8)
os.system('cls')
print("Aguarde..")
time.sleep(0.8)
os.system('cls')
print("Aguarde...")
time.sleep(0.8)
os.system('cls')
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
os.system('cls')
print("Fase 4: Jogo da Memória Mortal")
time.sleep(2)
os.system('cls')
print("Aguarde.")
time.sleep(0.8)
os.system('cls')
print("Aguarde..")
time.sleep(0.8)
os.system('cls')
print("Aguarde...")
time.sleep(0.8)
os.system('cls')
os.system('color 01') # Mudar o terminal para azul
print("Memorize a sequência de números que aparecerá na tela. Você terá 2 segundos para memorizar cada número.")
time.sleep(5)
os.system('cls')
sequencia1 = random.randint(1, 5)
sequencia2 = random.randint(1, 5)
sequencia3 = random.randint(1, 5)
sequencia4 = random.randint(1, 5)
sequencia5 = random.randint(1, 5)
print(sequencia1)
time.sleep(2)
os.system('cls')
print(sequencia2)
time.sleep(2)
os.system('cls')
print(sequencia3)
time.sleep(2)
os.system('cls')
print(sequencia4)
time.sleep(2)
os.system('cls')
print(sequencia5)
time.sleep(2)
os.system('cls')

