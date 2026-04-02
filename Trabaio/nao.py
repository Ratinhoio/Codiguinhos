# Responder apenas sim ou não para as perguntas abaixo
print("Responda as perguntas abaixo com 'sim' ou 'não'.")

# Perguntas
trabalho = input("Trabalha?")
estudo = input("Estuda?")
esporte = input("Pratica esportes?")

# Verificar as respostas
respotas = (trabalho, estudo, esporte)
contador = 0
for resposta in respotas:
    if resposta.lower() == "sim":
        contador += 1
if contador == 0:
    print("Tu é um preguiçoso") 
elif contador == 1:
    print("Tu é um pouco ativo")
elif contador == 2:
    print("Tu é um cara ocupado")
else:    print("Tu é um cara muito ativo")

