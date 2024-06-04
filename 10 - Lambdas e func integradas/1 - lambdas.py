"""
Lambdas

funções sem nome - anonimas

#FUNCAO EM PY
def soma(a, b):
    return a + b

def funcao(x):
    return 3 * x + 1
print (funcao(4))

#EXE LAMBDA
lambda x: x * 3 + 1 #não tem nome
calc = lambda x: x * 3 + 1 #variavel recebe lambda - não é o ideal.
print (calc(4))

#LAMBDA 2+ PARAMETROS
nome_completo = lambda nome, sobrenome: nome.strip().title()+' '+sobrenome.strip().title()
#strip - tira os espaços antes e após a string toda
#title - maiuscula a primeira letra

#EXEMPLOS#
voltinha = lambda: 'sai pra dar uma volta de carro e dei quantas?'
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: 3/ (1 / x+1 / y+1/ z)
print(voltinha)
print(duas(4, 5))
print(tres(8, 6, 3))

autores = ['Ana Carolina', 'João Pedro', 'Maria Eduarda', 'Lucas Gabriel', 'Julia Fernanda', 'Pedro Henrique', 'Luiz Felipe Silva', 'Mariana Santos Oliveira', 'André Costa Pereira', 'Ana Beatriz Almeida']

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
#split = pega cada os dados separados pelo espaço
#lower = tudo minúsculo

print (autores)

#funcao quadratica
def quadrado(a, b, c):
    #retorn a função f(x) = a * x ** 2 + b * x + c
    return lambda x: a*x**2 + b*x + c
"""






