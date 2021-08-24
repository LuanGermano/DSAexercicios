# # Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) e
# # depois faça uma chamada à função para listar os números


def pares1_20():
    par = []
    impar = []

    for n in range(1, 20):
        if n % 2 == 0:
            par.append(n)
        else:
            impar.append(n)
    return par


print(pares1_20())


# Exercício 2 - Crie uam função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string

def texto(palavra):
    return str(palavra).upper()


maiuscula = texto(input('Escreva uma palavra: '))
print(maiuscula)
# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e
# imprima a lista


def add_lista(lista):
    lista.append(2)
    lista.append(33)
    return lista


lista3 = list()
for c in range(0,4):
    lista3.append(str(input("Digite um parametro: ")))
nova_lista = add_lista(lista3)
print(nova_lista)

# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos.
# Faça duas chamadas à função, com apenas 1 elemento e na segunda chamada com 4 elementos

def exercicio4 (argumentoformal, *lista):
    print(argumentoformal)
    print(lista)
    return


exercicio4(100, 2, 5, 34, 'arnaldo')


# Exercício 5 - Crie uma função anônima e atribua seu retorno a uma variável chamada soma. A expressão vai receber 2
# números como parâmetro e retornar a soma deles
