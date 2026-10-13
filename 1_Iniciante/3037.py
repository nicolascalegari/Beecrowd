n = int(input())

for _ in range(n):
    pontos_joao = 0
    pontos_maria = 0

    for _ in range(3):
        x, d = map(int, input().split())
        pontos_joao += x * d

    for _ in range(3):
        x, d = map(int, input().split())
        pontos_maria += x * d

    if pontos_joao > pontos_maria:
        print("JOAO")
    else:
        print("MARIA")