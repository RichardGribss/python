import pandas as pd

produtos = 'produtos_mercado.csv'
df = pd.read_csv(produtos)

#adicionando nova coluna
df['Valor_Total_Estoque'] = df['Preco_Kg'] * df['Estoque_Kg']
print(df.head())

df_frutas = df[df['Categoria'] == 'Fruta']
df_frutas['Preco_Kg'] = df_frutas['Preco_Kg'] + ((df_frutas['Preco_Kg'] * 5) / 100)
print(df_frutas)

#adicionando status de peso
df['Status_Estoque'] = 'Médio'  # Valor padrão
df.loc[df['Estoque_Kg'] > 150, 'Status_Estoque'] = 'Alto'
df.loc[df['Estoque_Kg'] <= 50, 'Status_Estoque'] = 'Baixo'
print(df)