import random

cartela = []
numeros_usados = []

for i in range(5):
    linha = []
    for j in range(5):
        numero = random.randint(0, 99)
        while numero in numeros_usados:
            numero = random.randint(0, 99)
        numeros_usados.append(numero)
        linha.append(numero)
    cartela.append(linha)

print("Cartela de Bingo:")
for i in range(5):
    print(cartela[i])