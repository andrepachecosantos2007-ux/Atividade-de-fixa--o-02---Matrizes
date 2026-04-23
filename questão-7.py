matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

soma_impares = 0
for i in range(3):
    for j in range(3):
        if matriz[i][j] % 2 != 0:
            soma_impares = soma_impares + matriz[i][j]

print("Soma dos impares:", soma_impares)

for j in range(3):
    soma_coluna = 0
    for i in range(3):
        soma_coluna = soma_coluna + matriz[i][j]
    print(f"Soma da coluna {j}:", soma_coluna)

for i in range(3):
    soma_linha = 0
    for j in range(3):
        soma_linha = soma_linha + matriz[i][j]
    print(f"Soma da linha {i}:", soma_linha)