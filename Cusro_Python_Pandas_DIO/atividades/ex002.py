import pandas as pd

df1 = pd.read_excel("datasets\Aracaju.xlsx")
df2 = pd.read_excel("datasets\Fortaleza.xlsx")
df3 = pd.read_excel("datasets\dNatal.xlsx")
df4 = pd.read_excel("datasets\Recife.xlsx")
df5 = pd.read_excel("datasets\Salvador.xlsx")

df = pd.concat([df1, df2, df3, df4, df5])

print(df)
print(df.head(10))
print(df.tail(10))
print(df.isnull().sum())