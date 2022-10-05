import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')
pd.options.display.float_format = '{:20,.2f}'.format

df = pd.read_excel("datasets\AdventureWorks.xlsx")

# print(df)

# print(df.head(10))

# print(df.columns)

# print(df.dtypes)

# Qual a Receita total:
# print(df["Valor Venda"].sum())

#qual o custo total:
df["custo"] = df["Custo Unitário"].mul(df["Quantidade"]) #Criando a coluna custo
# print(df["custo"] )


# Custo Total
custo_total = round(df["custo"].sum(), 2)
# print(custo_total)

# Coluna lucro
df["Lucro"] = df["Valor Venda"] - df["custo"]
# print(df["Lucro"] )

# # Lucro Total
lucro_total = round(df["Lucro"].sum(), 2)
# print(lucro_total)

#criando uma coluna com total de dias para enviar o produto
df["Tempo_envio"] = df["Data Envio"] - df["Data Venda"]

#Extraindo apenas os diss
df["Tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days
# print(df.head(1))

#Media do tempo de envio por marca
media_envio_marca = df.groupby("Marca")["Tempo_envio"].mean()
# print(media_envio_marca)

#verificando se temos dados faltantes de
# print(df.isnull().sum())

#agrupar por ano e marca
lucro_ano_marca = df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum()
# print(lucro_ano_marca)

lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum().reset_index
# print(lucro_ano)

#Total produtos Vendidos
total_produtos_vendido = df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False)
# print(total_produtos_vendido)

#Grafico Total de Produtos vendidos
df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False).plot.barh(title='Total Produtos Vendidos')
# print(graf_total_produtos_vend)
plt.xlabel('Total')
plt.ylabel('Produto')