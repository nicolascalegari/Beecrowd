n = int(input())

fracao = 0.0

for _ in range(n):

    fracao = 1.0 / (6.0 + fracao)

resultado = 3 + fracao

print(f"{resultado:.10f}")