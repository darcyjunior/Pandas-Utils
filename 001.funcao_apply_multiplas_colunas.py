# Função Apply do Pandas para multiplas colunas
# Fonte: https://stackoverflow.com/questions/13331698/how-to-apply-a-function-to-two-columns-of-pandas-dataframe

import pandas as pd

df = pd.DataFrame({'ID': ['1', '2', '3'], 'col_1': [
                  0, 2, 3], 'col_2': [1, 4, 5]})
mylist = ['a', 'b', 'c', 'd', 'e', 'f']


def get_sublist(sta, end):
    return mylist[sta:end+1]


df['col_3'] = df.apply(lambda x: get_sublist(x.col_1, x.col_2), axis=1)

print(df)

# Se os nomes das colunas contiverem espaços ou compartilharem um nome com um atributo de dataframe existente,
# você poderá indexar com colchetes []:

df = pd.DataFrame({'ID': ['1', '2', '3'], 'col 1': [
                  0, 2, 3], 'col 2': [1, 4, 5]})

df['col 3'] = df.apply(lambda x: get_sublist(x['col 1'], x['col 2']), axis=1)

print(df)
