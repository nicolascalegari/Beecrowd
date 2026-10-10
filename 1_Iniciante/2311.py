n = int(input())

for _ in range(n):
    nome = input()
    grau_dificuldade = float(input())
    notas = list(map(float,input().split()))
    notas.remove(min(notas))
    notas.remove(max(notas))
    resultado_final =sum(notas) * grau_dificuldade
    print(f"{nome} {resultado_final:.2f}")
