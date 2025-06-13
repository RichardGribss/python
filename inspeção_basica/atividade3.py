import pandas as pd

produtos = 'produtos_mercado.csv'
df = pd.read_csv(produtos)

df['Data_Ultima_Reposicao'] = pd.to_datetime(df['Data_Ultima_Reposicao'])

print(df.dtypes)
