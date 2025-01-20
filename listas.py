# shallow copy

lista = [1, 2, 3, 4]

lista2 = lista

lista.append(100)

print(lista2)

# deep copy

lista = [1, 2, 3, 4]
lista2 = lista.copy()
lista.append(100)

print(lista2)

# função list()

# help(list)

# lista_string = list('Vinicius')
# type(lista_string)

# print(lista_string)

# dados = (1, 2, 3, 4, 5)

# print(type(dados))

# lista_tupla = list(dados)
# print(type(lista_tupla))
# print(lista_tupla)

# print(list())

lista_vazia = list()
print(lista_vazia)

lista_vazia = []
print(type(lista_vazia))
print(lista_vazia)

# count 
lista = [ 1,1,1,1,1,2,3,4,5,6,7,7,7,7,7,8,9,10 ]

print(lista.count(1))

# index

lista = ['python', 'java', 'c', 'visual basic','php','go lang', 'dephi']
lista.index('php')

print(lista)

print(lista[4])

print(lista[lista.index('php')])

# short

lista.sort()

print(lista)

lista.sort(reverse=True)

print(lista)

numeros = [10, 101, 134, 45, 12, 7,90]

numeros.sort()

print(numeros)

# reverse
print(lista)

lista.reverse()

print(lista)

print(dir(__builtins__))

lista = [1, 2, 3, 3, 'Python', 'Empowerdata']

print(len(lista))

# sum => soma (lista tem que ser apenas numeros)

lista = [1, 2, 3, 4, 5]

print(sum(lista))


# min => retorna o menor elemento (lista tem que ter apenas numeros!!!)
print(min(lista))

print(max(lista))

