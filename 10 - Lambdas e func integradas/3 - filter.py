"""
Filter

filter - filtrar dados de uma determinada coleção

import statistics
dados = [3.2, 5.4, 7.6, 9.6, 20, 14.5, 17.8, 16.0]
#média
media = statistics.mean(dados)
print(type(media))
#filter: 2 parametros - função e interável
res = filter(lambda x: x > media, dados)
print(list(res))
#obs: 'map' e 'filter' não armazenam dados

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', 'Equador', 'Venezuela', '', '']
print(paises)
res = filter(None, paises)
res = filter(lambda pais: len(pais) > 0, paises)
print(list(res))
res = filter(lambda pais: pais != '', paises)
"""

usuarios = [
    {"username": "Beatriz", "tweets": ["eu adoro bolo", "eu adoro pizza"]},
    {"username": "Arthur", "tweets": ["eu gosto de cachorro", "eu gosto de gato"]},
    {"username": "Matheus", "tweets": ["eu ando de bike", "eu ando de skate"]},
    {"username": "Rebeca", "tweets": []},
    {"username": "Bianca", "tweets": ["Muito Sucesso pra Você!"]},
]

#forma 1
inativos = list(filter(lambda user: len(user['tweets']) == 0, usuarios))

#forma 2
inativos = list(filter(lambda user: not user['tweets'], usuarios))
print(inativos)

#filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

lista = list(map(lambda nome: f'Sua instrutora é: {nome}', filter(lambda nome: len(nome) <= 5, nomes)))
print(lista)