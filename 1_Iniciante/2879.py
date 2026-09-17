n = int(input())

vitorias = 0

for _ in range(n):
    porta_carro = int(input())

    if porta_carro != 1:
        vitorias += 1

print(vitorias)