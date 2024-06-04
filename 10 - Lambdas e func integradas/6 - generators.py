"""

"""
#poderia ter sido feito com generators

nomes = ['Carlos', 'Robertos', 'Solange', 'Miguel', 'Larissa']
print(any(nome[0] == 'C' for nome in nomes))

print("----------------")

#list comprehension - se precisar da lista para alguma coisa
res = [nome[-1] == 's' for nome in nomes]
print(type(res))
print(res)
print("----------------")

#generator - apaga a memória, consultas rápidas (any)
res = (nome[-1] == "s" for nome in nomes)
print(type(res))
print(res)