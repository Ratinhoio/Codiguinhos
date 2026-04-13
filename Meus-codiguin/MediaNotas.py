notaGrau1 = (input("informe a nota do grau 1 de 0 a 10: "))
notaGrau1 = float(notaGrau1)
if notaGrau1 < 0 or notaGrau1 > 10:
    print("nota inválida, tente novamente")
    exit()
notaGrau2 = float(input("informe a nota do grau 2 de 0 a 10: "))
if notaGrau2 < 0 or notaGrau2 > 10:
    print("nota inválida, tente novamente")
    exit()
soma = notaGrau1 + notaGrau2
print("Agora vou te dizer se passou ou nao" + " com a média de " + str(soma / 2))
média = soma / 2
if média < 3:
    print("ai nao ne pae")
elif média < 7:
    print("ai, ta quase")
else:
    print("passou muleke")
# se juntar else com if da elif, é a mesma bosta
# usuário e senha para acessar o sistema, se o usuário for admin e a senha for 1234, acesso permitido, caso contrário, acesso negado
usuário= input("informe seu usuário: ")
senha = input("informe sua senha: ")

if usuário == "admin":
    if senha == "1234":
        print("Acesso permitido")
    else:
        print("Senha incorreta")
        quit()

usuário = input("informe seu usuário de novo: ")
senha = input("informe sua senha de novo: ")
if usuário == "admin" and senha == "1234":
    print("Acesso permitido")
else:
    print("Acesso negado, sai daqui!") 
    quit()

