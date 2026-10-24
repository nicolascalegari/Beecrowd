n, m = map(int, input().split())

matriz = []

for _ in range(n):
    matriz.append(list(map(int, input().split())))

coordenada_x = 0
coordenada_y = 0

for i in range(1, n - 1):
    for j in range(1, m - 1):
        if matriz[i][j] == 42:
            if (matriz[i-1][j-1] == 7 and matriz[i-1][j] == 7 and matriz[i-1][j+1] == 7 and
                matriz[i][j-1]   == 7                         and matriz[i][j+1]   == 7 and
                matriz[i+1][j-1] == 7 and matriz[i+1][j] == 7 and matriz[i+1][j+1] == 7):

                coordenada_x = i + 1
                coordenada_y = j + 1

    if coordenada_x != 0:
        break

print(f"{coordenada_x} {coordenada_y}")