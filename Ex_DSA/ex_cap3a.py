# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"
"""
dia = str(input("Qual dia da semana é hoje? ")).lower()
if dia == "sabado" or dia == "domingo":
    print('Hoje é dia de descanso')
else:
    print('Voce precisa trabalhar!')"""

# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista

cont3 = 0
lista1 = ['Abacaxi', 'Laranja', 'Pera', 'maçã', 'goiaba']
lista2 = ['Abacaxi', 'Laranja', 'Pera', 'maçã', 'morango']
for i in lista2:
    if i.lower() == "morango":
        cont3 += 1
if cont3 == 0:
    print('Não tem morango!')
else:
    print('Existe morango na lista')
# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma lista
tupla = (1,2,3,4)
lista3 = []
for i in tupla:
    lista3.append(i*2)
print(lista3)

# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela

for c in range(100,151,2):
    if c == 150:
        print(c)
    else:
        print(c, end=', ')
print()
# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35,
# imprima as temperaturas na tela
temperatura = 40
while temperatura > 35:
    print(temperatura, end=', ')
    temperatura -= 1
print()

# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa

contador = 0
while contador < 100:
    print(contador, end=', ')
    contador += 1
    if contador == 23:
        break
print()
# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20,
# adicione à lista, apenas os valores pares e imprima a lista
lista7 = []
var7 = 4
while var7 <= 20:
    if var7 % 2 == 0:
        lista7.append(var7)
        var7 +=1
    else:
        var7 +=1
print(lista7)

# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)
nums = range(5, 45, 2)
print(list(nums))

# Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.
temperatura = float(input('Qual a temperatura? '))
if temperatura > 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')

# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na   sua instrução de impressão
frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir."

for letra in range(0, len(frase)):
    if frase[letra] == 'r':
        contador += 1
print(f'Foram contados {contador} letras "r"')
