import pandas as pd

produtos = 'produtos_mercado.csv'
df = pd.read_csv(produtos)

#convertendo objeto para data
df['Data_Ultima_Reposicao'] = pd.to_datetime(df['Data_Ultima_Reposicao'])

#tipo de dado de cada coluna
print(df.dtypes)