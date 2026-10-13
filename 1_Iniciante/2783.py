n, c, m = map(int, input().split())

carimbadas = set(map(int, input().split()))

compradas = set(map(int, input().split()))

# Interseção
compradas_e_carimbadas = carimbadas & compradas

faltando = len(carimbadas) - len(compradas_e_carimbadas)

print(faltando)