import pandas as pd

produtos = 'produtos_mercado.csv'
df = pd.read_csv(produtos)

#coluna produto
print(df['Produto'])

print(df['Produto'],df['Categoria'],df['Preco_Kg'])

#achando o id 110
linha = df[df['ID_Produto'] == 110]
print(linha)

verduras = df[df['Categoria'] == 'Verdura']
print(verduras)

#kilo superior a R$:10,00
preco = df[df['Preco_Kg'] >= 10]
print(preco)

#Produtos repostos ma data 01/06/2024
data_determinada = df[df['Data_Ultima_Reposicao'] == '2024-06-01']
print(data_determinada)

fornecedor = df[df['Fornecedor'] == 'Fazenda Sol Nascente']
print(fornecedor)


filtrando = df[(df['Categoria'] == 'Fruta') | (df['Estoque_Kg'] >= 150)]
print(filtrando)