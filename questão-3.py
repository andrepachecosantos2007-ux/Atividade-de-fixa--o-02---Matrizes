matriz = []

for i in range(4):
    linha = []
    for j in range(4):
        linha.append(i * j)
    matriz.append(linha)

for i in range(4):
    print(matriz[i])