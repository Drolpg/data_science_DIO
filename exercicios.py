letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
nome = ["Leandro"]

print(letras[0])
print(nome[0])

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matriz[0][1])
for l in letras:
    print(l)


for i, letra in enumerate(letras):
    print(f"{i}: {letra}")
