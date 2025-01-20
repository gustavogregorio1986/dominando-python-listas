dados = dict(nome = 'Empowerdata', linguagem='Python', status=True)
print(type(dados))
print(dados)

lista = [ ('nome','Empowerdata'), ['linguagem','python'], ('status', True) ]
print(dict(lista))

dados = {}.fromkeys(['nome', 'linguagem','status'], ['Empowerdata', 'Python', True])

print(dados)

#get 

print(dados['linguagem']) 

