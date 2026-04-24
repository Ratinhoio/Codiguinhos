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
limpar()
print("Bem-vindo ao Pedra, Papel e Tesoura!")
input("Aperte Enter para começar ")
while pontos < 2 and pontospc < 2:
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
        limpar()
        print("Empatou")
    elif (jogada == "pedra" and pc == "tesoura") or (jogada == "papel" and pc == "pedra") or (jogada == "tesoura" and pc == "papel"):
        limpar()
        print("vOce ganhou!")
        pontos += 1
    else:
        limpar()
        print("pedeu:(")
        pontospc += 1
    dormir(2)
    print(f"Está {pontos} x {pontospc}")
    dormir(1)
    input("Da enter ai ")
if pontos == 2:
    limpar()
    print("ebaaaa, vc vencieu!")
    dormir(2)
    input("Da enter ai ")
    limpar()
elif pontospc == 2:
    limpar()
    print("Perdeu pra um compuitadorKKKKKKKKKKKK!")
    dormir(2)
    input("Da enter ai ")
    limpar()
