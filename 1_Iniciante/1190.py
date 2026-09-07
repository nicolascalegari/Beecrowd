operacao = input().strip()

matriz = []

for _ in range(12):
    linha = []
    for _ in range(12):
        linha.append(float(input()))
    matriz.append(linha)

soma = 0.0
elementos = 0

for j in range(7, 12):
    linha_inicio = 12 - j
    linha_fim = j

    for i in range(linha_inicio, linha_fim):
        soma += matriz[i][j]
        elementos += 1

if operacao == 'S':
    print(f"{soma:.1f}")
elif operacao == 'M':
    media = soma / elementos
    print(f"{media:.1f}")