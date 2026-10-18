linha_alvo = int(input())
operacao = input().strip()

matriz = []

for i in range(12):
    linha_atual = []
    for j in range(12):
        linha_atual.append(float(input()))
    matriz.append(linha_atual)

soma_linha = sum(matriz[linha_alvo])

if operacao == 'S':
    print(f"{soma_linha:.1f}")
elif operacao == 'M':
    media_linha = soma_linha / 12
    print(f"{media_linha:.1f}")