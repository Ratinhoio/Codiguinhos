import os, time, random, pygame
from datetime import datetime
def limpar():
    os.system("cls")
def aguarde(segundos):
    time.sleep(segundos)
def inicializarBancoDeDados():
    # r - read, w - write, a - append
    try:
        banco = open("base.jornaleiro","r")
    except:
        print("Banco de Dados Inexistente. Criando...")
        banco = open("base.jornaleiro","w")
