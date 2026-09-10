n, m = map(int, input().split())

for _ in range(m):

    acao = input().upper()

    if acao == "FECHOU":
        n += 1

    elif acao == "CLICOU":
        n -= 1

print(n)