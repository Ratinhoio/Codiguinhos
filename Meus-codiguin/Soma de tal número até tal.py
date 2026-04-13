print("Vou somar um por um até o menor número chegar até o maior número!")
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Guardar os números originais para exibir a diferença depois
n1 = numero1
n2 = numero2

if numero1 < numero2:
    while numero1 <= numero2:
        print(numero1)
        numero1 += 1
elif numero1 > numero2:
    while numero1 >= numero2:
        print(numero2)
        numero2 += 1
else:
    print("Os números são iguais, não há soma a ser feita.") 

print("A diferença entre os números é", abs(n1 - n2))
