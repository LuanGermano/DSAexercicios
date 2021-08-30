# exercicio de fazer uma calculadora que o usuario escolha entre 4 opções basicas e insira 2 numeros
def linha():
    print('=-=' * 17)


def leiaInt(msg):
    """
    Programa pra validação de inteiros
    :param msg: Valor recebido
    :return: saida do Int
    """
    while True:
        if msg.isnumeric():
            msg = int(msg)
            break
        else:
            print(f'\033[0;31mERRO! a Numero invalido.\033[m')
            msg = str(input('Digite a um valor numerico valido dentre as opções: '))
    return msg


# Inicio do Programa
operacoes = ['Soma', "Subtração", "Divisão", "Multiplicação"]

linha()
print('Escolha dentre as seguintes opções:')
for n in range(0, 4):
    print(n + 1, end='--')
    print(operacoes[n])
linha()


while True:
# interação do usuario
    opt = str(input("Digite qual conta quer selecionar [1/2/3/4]: "))
    opt = leiaInt(opt)
    if opt > 4:
        linha()
        print('\033[0;31mConta Selecionada invalida, por favor escolha entre uma das opções\033[m')
        linha()
    else:

        linha()
        n1 = float(input('Digite um valor: '))
        linha()
        n2 = float(input('Digite o segundo valor: '))
    # Programa
        if opt == 1:
            operacao = lambda x, y: n1 + n2
            print(f'O resultado da sua operação de {operacoes[opt-1]} desejada é: ')
            print(f'{n1} + {n2} = ', end='')
            print(operacao(n1, n2))
        elif opt == 2:
            operacao = lambda x, y: n1 - n2
            print(f'O resultado da sua operação de {operacoes[opt-1]} desejada é: ')
            print(f'{n1} - {n2} = ', end='')
            print(operacao(n1, n2))
        elif opt == 3:
            operacao = lambda x, y: n1 / n2
            print(f'O resultado da sua operação de {operacoes[opt-1]} desejada é: ')
            print(f'{n1} / {n2} = ', end='')
            print(operacao(n1, n2))
        elif opt == 4:
            operacao = lambda x, y: n1 * n2
            print(f'O resultado da sua operação de {operacoes[opt-1]} desejada é: ')
            print(f'{n1} * {n2} = ', end='')
            print(operacao(n1, n2))

        linha()
        cont = str(input("Deseja fazer mais alguma conta?[S/N]: ")).upper()
        linha()
        if cont == "N":
            print(f"{'Encerrando calculadora':^51}")
            linha()
            break
