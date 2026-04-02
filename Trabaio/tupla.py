'''
# tupla
tupla = (1, 2, 3, 4, 5)
print(tupla)
# tupla é imutável
# tupla[0] = 10 # isso vai dar erro
# tupla pode conter diferentes tipos de dados
tupla2 = (1, "dois", 3.0, True)
print(tupla2)
# tupla pode ser aninhada
tupla3 = (1, (2, 3), 4)
print(tupla3)
# tupla pode ser convertida para lista e vice-versa
lista = list(tupla)
print(lista)
tupla4 = tuple(lista)
print(tupla4)
# tupla pode ser usada para desempacotar valores
a, b, c, d, e = tupla
print(a, b, c, d, e)
# tupla pode ser usada para retornar múltiplos valores de uma função
def retorna_tupla():
    return 1, 2, 3
resultado = retorna_tupla()
print(resultado)
'''

# Mostrando um numero específico da tupla
from posixpath import curdir


tupla = (1, 2, 3, 4, 5)
print(tupla)
tupla = (10, 20, 30, 40, 50)
print(tupla[0])
print(tupla[1])

# Mostrando o tamanho da tupla com len()
print(len(tupla))

# Mostrando um intervalo de números da tupla
print(tupla[0:2])

# Concatenando tuplas
print(tupla + (60, 70, 80)) 

# Repetindo a tupla
print(tupla * 2) 

# Verificando se um elemento está na tupla
print(10 in tupla)
print(100 in tupla)

# Iterando sobre os elementos da tupla
for numero in tupla:
    print(numero)

# Contando quantas vezes um elemento aparece na tupla
print(tupla.count(10))

# Somando os elementos da tupla
print(tupla)
print(sum(tupla))

# Encontrando o valor mínimo e máximo da tupla
print(min(tupla))
print(max(tupla))

# Encontrando o índice de um elemento na tupla (posição do elemento)
print(tupla.index(30))

# Desempacotando os valores da tupla
a, b, c, d, e = tupla   
print(a, b, c, d, e)

# Ignorando valores ao desempacotar
print(a, c, e)

# Usando o operador * para desempacotar o restante dos valores
a, *resto, e = tupla
print(a, resto, e)

lista = [1, 2, 3, 4, 5]
for numero in lista:
    print(numero)
    print(lista[0])

# Range é uma função que gera uma sequência de números
for numero in range(1, 6):
    print(numero)
# Criar lista de usuários e adicionar um usuário a ela
usuarios = []
Alice = "Alice"
usuarios.append(Alice)
for usuario in usuarios:
    print(usuario)

nomes = input("Digite seu nome: ")
usuarios.append(nomes) 
for usuario in usuarios:
    print(usuario)

# Update na lista de usuários
