import os, random, time
def limpar():
    os.system('cls')
def dormir(segundos):
    time.sleep(segundos)
def efeito():
    print("Pedra...")
    dormir(1)
    print("Papel...")
    dormir(1)
    print("Tesoura...")
    dormir(1)
jogadas = ["pedra", "papel", "tesoura"]
pontos = 0
pontospc = 0
while True:
    limpar()
    jogada = input("Digite sua jogada> ").strip().lower()
    if jogada == "sair":
        break
    if not jogada in jogadas:
        limpar()
        print("não existe izo")
        input("Da enter ai ")
        continue
    pc = random.choice(jogadas)
    efeito()
    print(f"Pc jogou {pc}")
    dormir(2)
    if jogada == pc:
        print("Empatou")
    elif (jogada == "pedra" and pc == "tesoura") or (jogada == "papel" and pc == "pedra") or (jogada == "tesoura" and pc == "papel"):
        print("vOce ganhou!")
        pontos += 1
    else:
        print("pedeu:(")
        pontospc += 1
    dormir(2)
    print(f"Voce tem {pontos} pontos")
    input("Da enter ai ")
    if pontos == 2:
        break