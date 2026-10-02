while True:

    x = int(input())

    if x == 0:
        break

    if x % 2 != 0:
        x += 1

    soma = x + (x + 2) + (x + 4) + (x + 6) + (x + 8)

    print(soma)