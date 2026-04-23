respostas = []

for i in range(5):
    linha = []
    for j in range(10):
        resp = input(f"Aluno {i+1} - Questao {j+1}: ")
        linha.append(resp)
    respostas.append(linha)

gabarito = []
for j in range(10):
    g = input(f"Gabarito questao {j+1}: ")
    gabarito.append(g)

resultado = []
for i in range(5):
    pontos = 0
    for j in range(10):
        if respostas[i][j] == gabarito[j]:
            pontos = pontos + 1
    resultado.append(pontos)

for i in range(5):
    print(f"Aluno {i+1}: {resultado[i]} pontos")