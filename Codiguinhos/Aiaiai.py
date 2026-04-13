valor = 8
print(valor == 8)

# diferente true or false
print(valor != 10)
print(valor != 8)
print('ATITUS' == 'atitus')
print(123 != 456)
print(100 < 200)
print('a' < 'b')
print(10 >= 10)
print(10 <= 10)
import os, time
os.system('cls')
while True:
    try:
        resposta = int(input("Quanto é 2+2? "))
        break
    except:
        print("Digite apenas números!")
        input("Pressione Enter para tentar de novo...")
        os.system('cls')

if resposta == 4:
        print("yey")
    