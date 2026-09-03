valores = list(map(int, input().split()))

a = valores[0]

for i in range(1, len(valores)):
    if valores[i] > 0:
        n = valores[i]
        break

soma = 0

for i in range(n):
    soma += a + i

print(soma)
