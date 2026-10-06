n = int(input())

melhor_aluno = None
maior_nota = -1.0

for _ in range(n):
    entrada = input().split()
    matricula = int(entrada[0])
    nota = float(entrada[1])

    if nota > maior_nota:
        maior_nota = nota
        melhor_aluno = matricula

if maior_nota >= 8.0:
    print(melhor_aluno)
else:
    print("Minimum note not reached")