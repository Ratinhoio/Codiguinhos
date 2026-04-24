import os, random, time
def limpar():
    os.system('cls')
def dormir(segundos):
    time.sleep(segundos)

jogadas = ["pedra", "papel", "tesoura"]
while True:
    limpar()
    jogada = input("Digite sua jogada> ")
    if not jogada in jogadas:
        limpar()
        print("não existe izo")
        input("Da enter ai ")
        continue
    pc = random.choice(jogadas)
    print(f"Pc jogou {pc}")
    dormir(2)
    if jogada == pc:
        print("Empatou")
    elif (jogada == "pedra" and pc == "tesoura") or (jogada == "papel" and pc == "pedra") or (jogada == "tesoura" and pc == "papel"):
        print("vOce ganhou!")
    else:
        print("pedeu:(")
    dormir(2)