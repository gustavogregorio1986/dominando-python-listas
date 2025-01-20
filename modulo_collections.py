from collections import Counter

lista = [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 6, 7, 7, 7, 7, 8, 9]

contador = Counter(lista)
print(type(contador))
print(contador)

nome = 'Vinicius'
print(Counter(nome))

texto = """
Eu te amo porque te amo,
Não precisas ser amante,
e nem sempre sabes sê-lo.
Eu te amo porque te amo.
Amor é estado de graça
e com amor não se paga.

Amor é dado de graça,
é semeado no vento,
na cachoeira, no eclipse.
Amor foge a dicionários
e a regulamentos vários.

Eu te amo porque não amo
bastante ou demais a mim.
Porque amor não se troca,
não se conjuga nem se ama.
Porque amor é amor a nada,
feliz e forte em si mesmo.

Amor é primo da morte,
e da morte vencedor,
por mais que o matem (e matam)
a cada instante de amor.
"""

print(texto)

print(Counter(texto.lower().split()))

print(contador.keys())

print(contador.values())

print(contador.items())

print(contador.most_common())

print(contador.most_common(1))

print(contador.most_common(3))

from collections import defaultdict

dados = defaultdict(list)

print(dados)

dados["nome"] = 'Vinicius'

dados["sobrenome"]

print(dados)

print(texto.lower())

for i in texto.lower().split():
    dados[i].append(i)


print(dados)

from collections import OrderedDict

dict_a = {'a':1, 'b':1}
dict_b = {'b':2, 'a':1}

print(dict_a == dict_b)