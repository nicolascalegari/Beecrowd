n, m = map(int, input().split())

frutas = []
for _ in range(n):
    frutas.append(input().lower())

texto_completo = ""
for _ in range(m):
    texto_completo += input().lower()

for fruta in frutas:
    fruta_invertida = fruta[::-1]

    if fruta in texto_completo or fruta_invertida in texto_completo:
        print(f"Sheldon come a fruta {fruta}")
    else:
        print(f"Sheldon detesta a fruta {fruta}")