gabarito = []
for j in range(10):
    g = input(f"Gabarito questao {j+1}: ")
    gabarito.append(g)

for i in range(3):
    matricula = int(input(f"Matricula do aluno {i+1}: "))
    nota = 0
    for j in range(10):
        resp = input(f"Aluno {i+1} - Questao {j+1}: ")
        if resp == gabarito[j]:
            nota = nota + 1
    print(f"Matricula: {matricula} - Nota: {nota}")