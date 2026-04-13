import pyttsx3
def falar(texto):
    motor = pyttsx3.init()
    motor.say(texto) 
    motor.runAndWait()

print("Responda as perguntas com s para sim e n para não")
falar("Telefonou o suspeito?")
telefone = input("Telefonou o suspeito? (s/n) ")
if telefone.lower() != "s" and telefone.lower() != "n":
    print("Resposta inválida, tente novamente")
    exit()

falar("Esteve no local do crime?")
local = input("Esteve no local do crime? (s/n) ")
if local.lower() != "s" and local.lower() != "n":
    print("Resposta inválida, tente novamente")
    exit()

falar("Mora perto da vítima?")
moraPerto = input("Mora perto da vítima? (s/n) ")
if moraPerto.lower() != "s" and moraPerto.lower() != "n":
    print("Resposta inválida, tente novamente")
    exit()

falar("Devia para a vítima?")
devia = input("Devia para a vítima? (s/n) ")

if devia.lower() != "s" and devia.lower() != "n":
    print("Resposta inválida, tente novamente")
    exit()

falar("Já trabalhou com a vítima?")
trabalhou = input("Já trabalhou com a vítima? (s/n) ")
if trabalhou.lower() != "s" and trabalhou.lower() != "n":
    print("Resposta inválida, tente novamente")
    exit()

respostas = [telefone, local, moraPerto, devia, trabalhou]
contador = 0
for resposta in respostas:
    if resposta.lower() == "s":
        contador += 1
if contador == 2:
    print("Tu é SUSPEITO")
elif contador == 3 or contador == 4:
    print("Tu é CÚMPLICE")
elif contador == 5:
    print("Tu é ASSASSINO")
else:
    print("Tu é INOCENTE")

if telefone.lower() == "s":
    print("Qual o número do telefone?")
    numeroTele = input("Digite o número do telefone: ")


if local.lower() == "s":
    print("Qaul é o local do crime?")
    localCrime = input("Digite o local: ")

if moraPerto.lower() == "s":
    print("Qual é o endereço da vítima?")
    endereço = input("Digite o endereço: ")

if devia.lower() == "s":
    print("Quanto devia para a vítima?")
    valor = input("Digite o valor: ")

if trabalhou.lower() == "s":
    print("Qual era o cargo do suspeito na empresa?")
    cargo = input("Digite o cargo: ")
    