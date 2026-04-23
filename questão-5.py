matriz = []

for i in range(5):
    linha = []
    for j in range(5):
        valor = int(input(f"Elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

x = int(input("Digite o valor a buscar: "))

encontrado = False
for i in range(5):
    for j in range(5):
        if matriz[i][j] == x:
            print("Encontrado na linha", i, "coluna", j)
            encontrado = True

if encontrado == False:
    print("Nao encontrado")