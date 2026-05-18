import os, time
dados = []
try:
    arquivo = open("bd.atitus", "r") # r - w - a
    dados = arquivo.readlines()
    arquivo.close()
except:
    arquivo = open("bd.atitus", "w") # r - w - a
    arquivo.close()


while True:
    os.system("cls")
    print("(1) - Inserir Novo Nome")
    print("(2) - Listar Nomes")
    print("(0) - Sair")
    op = input()
    if op == "1":
        nome = input("Informe o nome:")
        dados.append(nome)
        
        arquivo = open("bd.atitus", "a") # r - w - a
        arquivo.write(nome+"\n")
        arquivo.close()
        
        print("Dados Salvos!")
        time.sleep(2)
    elif op == "2":
        print("Nomes Salvos:")
        for nome in dados:
            print(f"Nome: {nome}")
        time.sleep(3)
    elif op == "0":
        break
    else:
        print("Opção Inválida!")
        time.sleep(2)
        