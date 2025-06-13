import pandas as pd

produtos = 'produtos_mercado.csv'
df = pd.read_csv(produtos)

#número de linhas e colunas
linhas, colunas = df.shape
print(f"Linhas: {linhas}, Colunas: {colunas}")