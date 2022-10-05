import pandas as pd

df = pd.read_csv("datasets\Gapminder.csv", error_bad_lines=False, sep=';')
# df = pd.DataFrame({'num_legs': [2, 4], 'num_wings': [2, 0]}, index=['falcon', 'dog'])
df = df.rename(columns={"country":"Pais", "continent":"Continente", "year":"Ano", "lifeExp":"Expectativa de vida", "pop":"Pop total", "gdpPercap":"PIB"})


print(df)
print(df.shape)
print(df.columns)
print(df.head(10))
print(df.dtypes)
print(df.tail(10))
print(df.describe())
print(df["Continente"].unique)
Oceania = df.loc[df["Continente"] == "Oceania"]
print(Oceania.head(5))

print(df.groupby('Continente')['Pais'].nunique())
print(df.groupby('Ano')['Expectativa de vida'].mean())