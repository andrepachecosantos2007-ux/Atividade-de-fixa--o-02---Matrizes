a = []
b = []
c = []

print("--- Matriz A ---")
for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input(f"A[{i}][{j}]: "))
        linha.append(valor)
    a.append(linha)

print("--- Matriz B ---")
for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input(f"B[{i}][{j}]: "))
        linha.append(valor)
    b.append(linha)

for i in range(4):
    linha = []
    for j in range(4):
        if a[i][j] > b[i][j]:
            linha.append(a[i][j])
        else:
            linha.append(b[i][j])
    c.append(linha)

print("Matriz C:")
for i in range(4):
    print(c[i])