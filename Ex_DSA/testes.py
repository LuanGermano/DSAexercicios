#help(map)
#help(dir)

#dicionario = {'ola': 'mundo', 'curso': 'Datascientistacademy'}
#print(dicionario)
#dir(dicionario)

#dic = {'k1': 'Natal', 'k2': 'Recife'}
#dir(dic)

# Exercício 9
# Abaixo você encontra a importação do Pandas, um dos principais pacotes Python para análise de dados.
# Analise atentamente todos os métodos disponíveis. Um deles você vai usar no próximo exercício.

# Exercício 10 - Crie uma função que receba o arquivo abaixo como argumento e retorne um resumo estatístico descritivo
# do arquivo. Dica, use Pandas e um de seus métodos, describe()
# Arquivo: "binary.csv"

import pandas as pd
file_name = "binary.csv"


def retornaArq(file_name):
    df = pd.read_csv(file_name)
    return df.describe()


retornaArq(file_name)  # ??