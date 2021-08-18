# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla
# Exercício 5 - Crie um dicionário vazio e imprima na tela
# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos.
# Imprima o dicionário na tela.

# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string,
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'

lista1 = []
for c in range(1, 11):
    lista1.append(c)
print(lista1)

lista2 = ['ola', "mundo", 'eu n devia misturar aspas', 'pq dps isso é ruim', 'mas respondi']
print(lista2)

a = 'olá, '
b = 'mundo'
print(a + b)

tupla1 = (1, 2, 2, 3, 4, 4, 4, 5)
print(tupla1.count(4))

ex5 = dict()
print(ex5)

ex6 = {'Chave1': 1, 'chave2': 2, 'chave3': 3}
print(ex6)
ex6['chave4']= 4
print(ex6)

ex8 =ex6 = {'Chave1': 1, 'chave2': 2, 'lista de numeros': [1,2]}
print(ex8)

ex9 = ['Amendoim',('Castanha','Caju'),{'Chave1': 1, 'chave2': 2}, 3.5]
print(ex9)

print(frase[0:18])