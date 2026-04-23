matriz = []

for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input(f"Elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

contador = 0
for i in range(4):
    for j in range(4):
        if matriz[i][j] > 10:
            contador = contador + 1

print("Valores maiores que 10:", contador)