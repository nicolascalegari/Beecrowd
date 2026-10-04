operacao = input().strip()

matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

soma = 0.0
total_elementos = 0

for i in range(12):
    for j in range(12):
        if j < i and j < 11 - i:
            soma += matriz[i][j]
            total_elementos += 1

if operacao == 'S':
    print(f"{soma:.1f}")
elif operacao == 'M':
    media = soma / total_elementos
    print(f"{media:.1f}")