operacao = input().strip()

soma = 0.0
elementos_contados = 0

for i in range(12):
    for j in range(12):
        valor = float(input())

        if j > i:
            soma += valor
            elementos_contados += 1

if operacao == 'M':
    resultado = soma / elementos_contados
else:
    resultado = soma

print(f"{resultado:.1f}")