# Missão Espacial
combustivel = int(input("Nível de combustível (0-100): "))
tripulacao = int(input("Número de tripulantes: "))
temp = int(input("Temperatura (°C): "))
ia = input("IA ativa? (s/n): ")
# verificar se a missão é proibida
if combustivel < 20:
 print("Missão proibida")
elif temp < -80:
    print("Missão proibida")
elif temp > 120:
    print("Missão proibida")
# verificar se a missão é perigosa
elif combustivel >= 20 and combustivel <= 40:
    print("Missão perigosa")
elif tripulacao < 2:
    print("Missão perigosa")
elif ia.lower() == "n":
    print("Missão perigosa")
# verificar se a missão tem risco controlado
elif combustivel >= 40 and combustivel <= 70 and temp >= 20 and temp <= 80:
    print("Missão com risco controlado")
# verificar se a missão é segura
elif combustivel > 70 and tripulacao >= 3 and ia.lower() == "s":
    print("Missão segura")
# extras
else:
    print("Depende")

    
    
    
    
    
    
    
    
    
    
    