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