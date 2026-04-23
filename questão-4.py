matriz = []

for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input(f"Elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

print("Matriz:")
for i in range(4):
    print(matriz[i])

maior = matriz[0][0]
linha_maior = 0
coluna_maior = 0

for i in range(4):
    for j in range(4):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            linha_maior = i
            coluna_maior = j

print("Maior valor:", maior)
print("Linha:", linha_maior, "Coluna:", coluna_maior)