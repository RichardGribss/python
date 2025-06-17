import pandas as pd

produtos = 'produtos_mercado.csv'
df = pd.read_csv(produtos)

#quantos dados nulos cada coluna tem
print(df.isna().sum())

#atualizando o preço do morango pela média
quantidade_frutas = df['Produto'].count()
preco_medio = (df['Preco_Kg'].sum()) / quantidade_frutas
df.loc[df['Produto'] == 'Morango', 'Preco_Kg'] = preco_medio
print(df.loc[df['Produto'] == 'Morango'])

df.loc[df['Produto'] == 'Kiwi', 'Estoque_Kg'] = 0

print(df.isna().sum())