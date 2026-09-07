while True:

    n = int(input())

    if n == 0:
        break

    for i in range(n):

        linha = []

        for j in range(n):

            valor = abs(i - j) + 1

            linha.append(f"{valor:3d}")

        print(" ".join(linha))

    print()