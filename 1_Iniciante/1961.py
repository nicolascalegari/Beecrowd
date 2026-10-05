pulo, num_canos = map(int, input().split())

alturas = list(map(int, input().split()))

ganhou = True

for i in range(num_canos - 1):
    diferenca = abs(alturas[i + 1] - alturas[i])

    if diferenca > pulo:
        ganhou = False
        break

if ganhou:
    print("YOU WIN")
else:
    print("GAME OVER")
