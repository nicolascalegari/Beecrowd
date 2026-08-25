cont1 = 0
cont2 = 0
while cont2 < 6:
    valor = float(input())
    if valor > 0:
        cont1 += 1
    cont2 += 1

print(f"{cont1} valores positivos")