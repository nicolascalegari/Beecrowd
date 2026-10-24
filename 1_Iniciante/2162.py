n = int(input())

h = list(map(int, input().split()))

padra_valido = 1

if n > 1:
    ultimo_movimento = ""
    if h[1] > h[0]:
        ultimo_movimento = "subiu"
    elif h[1] < h[0]:
        ultimo_movimento = "desceu"
    else:
        padra_valido = 0

    for i in range(2, n):
        if padra_valido == 0:
            break

        if h[i] > h[i - 1]:
            if ultimo_movimento == "subiu":
                padra_valido = 0
            ultimo_movimento = "subiu"

        elif h[i] < h[i - 1]:
            if ultimo_movimento == "desceu":
                padra_valido = 0
            ultimo_movimento = "desceu"

        else:
            padra_valido = 0

print(padra_valido)