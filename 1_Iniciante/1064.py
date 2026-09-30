soma = 0
qtd = 0

for _ in range(6):

    num = float(input())


    if num > 0.0:
        qtd += 1
        soma += num

media = soma / qtd

print(f"{qtd} valores positivos")
print(f"{media:.1f}")