"""
Maps

mapeamento de valores para função

import math
#material
def area(r):
    return math.pi * (r ** 2)
raios = [2, 5, 7.1, 8.2, 34, 1, 1.4]
areas = []
#forma 1 - normal
for r in raios:
    areas.append((area(r)))
print(areas)

#forma 2 - map
#map é uma função que recebe dois parâmetros: função, interavel. retorna um map object
areas = map(area, raios)
print(list(areas))
#forma 3 - map com lambda
print(list(map(lambda r: math.pi * (r**2), raios)))
"""
cidades = [('Leme', 26), ('Limeira', 31), ('Araras', 18), ('Pirassununga', 30), ('Porto Ferreira', 33), ('Campinas', 35), ('Rio Claro', 15), ('Corderópolis', 19), ('Santa Cruz', 20)]

c_para_f = lambda dado:(dado[0], (9/5) * dado[1] + 32)

print(list(map(c_para_f, cidades))) 