# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"

dia = str(input("Qual dia da semana é hoje? ")).lower()
if dia == "sabado" or dia == "domingo":
    print('Hoje é dia de descanso')
else:
    print('Voce precisa trabalhar!')

