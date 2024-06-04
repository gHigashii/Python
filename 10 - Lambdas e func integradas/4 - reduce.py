"""
Reduce

A partir do Py3 a função reduce não é mais uma função integrada (built-in). Agora temos que importar e utilizar esta função a partir do módulo 'functools'

Reduce somente quando necessário, 99% é loop for

para entender o reduce()

dados=[10, 20, 30, 40, 50]

def func(x, y):
    return x + y

reduce (funcao, dados):
passo 1: res1 = f(a1, a2) 
passo 2: res2 = f(res1, a3)
passo 3: res3 = f(res2, a4)

---------------------------------------------------
from functools import reduce

dados
dados = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

função
multi = lambda x, y: x * y

função e dados com reduce
res = reduce(multi, dados)
print(res)

---------- OU ----------
for n in dados:
    res = res * n
print(res)
"""


