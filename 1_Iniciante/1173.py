n = int(input())

lista = []
lista.append(n)

i = 1
j = 0
for i in range(10):

    n *= 2
    lista.append(n)
    print(f"N[{j}] = {lista[i]}")
    j += 1