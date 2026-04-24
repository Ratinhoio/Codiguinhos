# Criar um codigo pra impressionar minha cacheada
import time, os, random
def limpar():
    os.system('cls')
def dormir(segundos):
    time.sleep(segundos)
limpar()
contador = 0
print("Oi, amor! Eu fiz esse código só pra te impressionar!")
def elogios():
    global contador
    elogios = [
        "Você é a pessoa mais incrível que eu já conheci!",
        "Seu sorriso ilumina meu dia!",
        "Eu me sinto muito sortudo por ter você na minha vida!",
        "Você é linda por dentro e por fora!",
        "Eu te amo mais do que palavras podem expressar!",

        "Você tem um jeito que acalma tudo em mim",
        "Quando eu falo com você, meu dia já melhora",
        "Você é tipo um lugar seguro pra mim",
        "Eu fico pensando em você do nada o tempo todo",
        "Você é diferente de todo mundo, e isso é perfeito",

        "Seu sorriso devia ser patrimônio mundial",
        "Você fica linda até sem tentar",
        "Eu gosto até das suas manias",
        "Até seus defeitos são bonitos pra mim",
        "Você tem um jeito que prende minha atenção fácil",

        "Você é minha paz no meio do caos",
        "Conversar contigo é uma das melhores partes do meu dia",
        "Eu poderia ficar horas só te ouvindo",
        "Você faz as coisas simples parecerem especiais",
        "Eu me sinto bem sendo eu mesmo com você",

        "Você é tipo meu conforto favorito",
        "Seu abraço devia ser proibido de tão bom",
        "Você tem um brilho diferente",
        "Eu admiro muito o teu jeito",
        "Você me inspira mais do que imagina",

        "Você é bonita de um jeito que não dá pra explicar direito",
        "Eu gosto de você em todos os seus jeitos",
        "Você consegue ser fofa e incrível ao mesmo tempo",
        "Eu daria replay em qualquer momento contigo",
        "Você faz falta mesmo quando acabou de sair",

        "Você é minha pessoa favorita fácil",
        "Eu gosto de tudo quando envolve você",
        "Você deixa tudo mais leve",
        "Você é tipo uma calmaria boa",
        "Eu gosto da forma como você vê as coisas",

        "Você é especial num nível absurdo",
        "Eu tenho orgulho de ter você comigo",
        "Você é importante pra mim de um jeito que nem sei explicar",
        "Eu escolheria você de novo sem pensar",
        "Você é a melhor parte dos meus dias",

        "Você é meu pensamento favorito",
        "Eu gosto de você mais do que deveria (e ainda acho pouco)",
        "Você tem um jeito que me ganha sempre",
        "Eu me apego fácil em você, fazer o quê",
        "Você tem um efeito em mim que eu não sei explicar",

        "Você é tipo vício, mas dos bons",
        "Você me faz sorrir sem nem perceber",
        "Eu fico besta com você fácil",
        "Você tem algo que ninguém mais tem",
        "Eu gosto de você num nível preocupante",

        "Você é minha coincidência favorita",
        "Eu gosto do jeito que você existe",
        "Você tem uma presença que muda tudo",
        "Você é o tipo de pessoa que vale a pena",
        "Você faz meu mundo ficar melhor só por estar nele",

        "Você é tipo uma sorte boa que apareceu",
        "Eu não enjoo de você nunca",
        "Você é minha escolha favorita",
        "Eu gosto de você até quando tô bravo (o que é raro)",
        "Você é diferente… e isso é o que eu mais gosto"
        ]
    while True:
        elogio = random.choice(elogios)
        limpar()
        for letra in elogio:
            print(letra, end='', flush=True)
            dormir(0.10)
        contador += 1
        print("\n")
        dormir(2)
        print("Você já recebeu " + str(contador) + " elogios até agora! E tem muito mais vindo por aí!")
        input("Pressione Enter para receber outro elogio...")
def detector():
    limpar()
    print("Vamos descobrir o quão incrível você é!")
    dormir(1)
    print("Analisando personalidade...")
    porcentagem = random.randint(0, 100)
    dormir(2)
    limpar()
    print(f"De acordo com meus cálculos, você é 1% incrível!")
    dormir(3)
    input("Ops, me confundi, posso tentar tentar de novo?... 👉👈 ")
    limpar()
    print(f"De acordo com meus cálculos, você é {porcentagem}% incrível!")
    dormir(2)
    input("Pressione Enter para continuar...")
def quiz():
    limpar()
    print("Vamos ver seu conhecimento!")
    dormir(2)
    limpar()
    resposta1 = input("Quem é mais sapeca? ")
    if resposta1 == "voce":
        print("Ainda bem que sabe")
    elif resposta1 == "eu":
        print("Hahahah, essa foi boa. Mas ta errado")
    else:
        print("??????")
    input("Enter para proxima pergunta!")
    limpar()
    resposta2 = input("Quem manda mais reels? ")
    if resposta2 == "voce":
        print("Nada ve fia")
    elif resposta2 == "eu":
        print("AcertouKKKKKKK")
    else:
        print("??????")
    input("Enter para proxima pergunta!")
    limpar()
    resposta3 = input("Quem se apaixonou primeiro? ")
    if resposta3 == "voce":
        print("SabiaKKKKKK")
    elif resposta3 == "eu":
        print("Hmmmmmmmmm, suspeito mas aceito")
    else:
        print("??????")
    input("Enter para proxima pergunta!")
    limpar()
    resposta4 = input("Quem é mais ciumento(a)? ")
    if resposta4 == "eu":
        print("Concordo")
    elif resposta4 == "voce":
        print("eu??????")
    else:
        print("?????")  

def menu():
    while True:
        limpar()
        print("1 - Elogios")
        print("2 - Detector")
        print("3 - Quiz")
        escolha = input("O que você quer? > ")
        if escolha == "1":
            elogios()
            break
        elif escolha == "2":
            detector()
            break
        elif escolha == "3":
            quiz()
            break
        else:
            limpar()
            print("Escolha inválida, por favor tente novamente.")
            dormir(2)
menu()