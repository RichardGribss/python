import pandas as pd

produtos = 'produtos_mercado.csv'
df = pd.read_csv(produtos)

print(df.head(7))