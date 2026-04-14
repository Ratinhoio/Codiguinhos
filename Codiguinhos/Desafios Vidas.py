import os, random, time
# Usando time melhor
for i in range(5, 0, -1):
    os.system('cls')
    print(f"⏰ Responda em {i}...")
    time.sleep(1)

inicio = time.time()
resposta = input("Você é viadin? ")
fim = time.time()
tempoTotal = fim - inicio
print (f"Você demorou {tempoTotal:.0f} segundos")

resposta = input("Quanto é 2+2? ")


