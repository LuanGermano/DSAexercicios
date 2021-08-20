# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"

dia = str(input("Qual dia da semana é hoje? ")).lower()
if dia == "sabado" or dia == "domingo":
    print('Hoje é dia de descanso')
else:
    print('Voce precisa trabalhar!')

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
tupla = ()
