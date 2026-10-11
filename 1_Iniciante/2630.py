t = int(input())

for i in range(1, t+1):
    conversao = input()

    r, g, b = map(int, input().split())

    if conversao == "min":
        resultado = min(r, g, b)
    elif conversao == "max":
        resultado = max(r, g, b)
    elif conversao == "mean":
        resultado = (r + g + b) // 3
    elif conversao == "eye":
        resultado = int(0.30 * r + 0.59 * g + 0.11 * b)

    print(f"Caso #{i}: {resultado}")