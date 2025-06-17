import pandas as pd

produtos = 'produtos_mercado.csv'
df = pd.read_csv(produtos)

#ordem alfabetica
print(df.sort_values('Produto'))

#mais caros
print(df.sort_values(by='Preco_Kg', ascending=False))

#produtos mais frescos em ordem alfabeticas
df_ordenado = df.sort_values(by=['Data_Ultima_Reposicao', 'Produto'], ascending=[False, True])
print(df_ordenado[['Produto', 'Data_Ultima_Reposicao']])