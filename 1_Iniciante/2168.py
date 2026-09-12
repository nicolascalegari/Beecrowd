n = int(input())

matriz = []

for _ in range(n + 1):
    linha = list(map(int, input().split()))
    matriz.append(linha)

for i in range(n):
    resul_linha = []
    for j in range(n):
        cameras = (matriz[i][j] +
                  matriz[i][j+1] +
                  matriz[i+1][j] +
                  matriz[i+1][j+1])

        if cameras >= 2:
            resul_linha.append("S")
        else:
            resul_linha.append("U")

    print("".join(resul_linha))