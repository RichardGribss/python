import pandas as pd

produtos = 'produtos_mercado.csv'
df = pd.read_csv(produtos)

frutas = df.loc[df['Categoria'] == 'Fruta']
print(frutas.count())

media_por_categoria = df.groupby('Categoria')['Preco_Kg'].mean().round(2).reset_index()
print(media_por_categoria)

media_por_categoria = df.groupby('Fornecedor')['Estoque_Kg'].sum().round(2).reset_index()
print(media_por_categoria)