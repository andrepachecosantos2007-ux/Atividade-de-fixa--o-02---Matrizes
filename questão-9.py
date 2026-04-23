distancias = [
    [0, 15, 30, 5, 12],
    [15, 0, 10, 17, 28],
    [30, 10, 0, 3, 11],
    [5, 17, 3, 0, 80],
    [12, 28, 11, 80, 0]
]

c1 = int(input("Digite a cidade de origem (0 a 4): "))
c2 = int(input("Digite a cidade de destino (0 a 4): "))
print("Distancia:", distancias[c1][c2], "km")

total = 0
for k in range(6):
    i = int(input(f"Coordenada {k+1} - linha: "))
    j = int(input(f"Coordenada {k+1} - coluna: "))
    total = total + distancias[i][j]

print("Total percorrido:", total, "km")