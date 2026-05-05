import os
import time
while True:
    os.system("cls")
    contadorDicas = 0
    totalErros = 0
    desafiante = input("Nome do Desafiante: ")
    competidor = input("Nome do Competidor: ")
    os.system("cls")
    palavra = input("Palavra Chave: ")
    secreta = "*" * len(palavra)
    dica1 = input("Dica1: ")
    dica2 = input("Dica2: ")
    dica3 = input("Dica3: ")