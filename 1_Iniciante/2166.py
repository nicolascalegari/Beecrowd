n = int(input())

fracao = 0.0

for _ in range(n):

    fracao = 1.0 / (2.0 + fracao)

resultado = 1.0 + fracao

print(f"{resultado:.10f}")