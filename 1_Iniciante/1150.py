x = int(input())

while True:

    z = int(input())

    if z > x:
        break

soma = 0
qtd = 0
atual = x

while soma <= z:

    soma += atual
    atual += 1
    qtd += 1

print(qtd)