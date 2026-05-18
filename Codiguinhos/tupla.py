import os, time
os.system("cls")
telefones = {"Maria": "384917234981273", "Pedro": "218013242342", "Carlos": "12893712398"}
nome = input("Coloque o nome ai prr:")
'''
while True:
    try:
        print(telefones[nome])
        break
    except:
        print("nem existe izo ae")
'''
telefones["Tomas"] = "123123123123" #Adicionar
telefones.pop("Tomas")
print(telefones.get(nome, "Pessoa não encotrada"))


# tupla, lista e dicionario

