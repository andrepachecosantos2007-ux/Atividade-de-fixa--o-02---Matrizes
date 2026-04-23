matriz = [
    [8, 0, 7],
    [4, 5, 6],
    [3, 10, 2]
]

somas = []

for i in range(3):
    soma = 0
    for j in range(3):
        soma = soma + matriz[i][j]
    somas.append(soma)

for j in range(3):
    soma = 0
    for i in range(3):
        soma = soma + matriz[i][j]
    somas.append(soma)

diag_principal = 0
diag_secundaria = 0
for i in range(3):
    diag_principal = diag_principal + matriz[i][i]
    diag_secundaria = diag_secundaria + matriz[i][2 - i]

somas.append(diag_principal)
somas.append(diag_secundaria)

magico = True
for i in range(1, len(somas)):
    if somas[i] != somas[0]:
        magico = False

if magico:
    print("E um quadrado magico!")
else:
    print("Nao e um quadrado magico.")