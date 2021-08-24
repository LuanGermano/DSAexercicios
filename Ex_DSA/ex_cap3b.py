# # Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) e
# # depois faça uma chamada à função para listar os números
par = []
impar = []

for n in range(1, 20):
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

print(*impar)
print(*par)

# Exercício 2 - Crie uam função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string

texto = str(input("Escreva uma palavra: "))

print(texto.upper())

# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e
# imprima a lista

lista = (1,2,3,4)
