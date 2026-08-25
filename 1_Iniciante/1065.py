cont1 = 0
cont2 = 0
while cont2 < 5:
    valor = int(input())
    if valor % 2 == 0:
        cont1 += 1
    cont2 += 1

print(f"{cont1} valores pares")