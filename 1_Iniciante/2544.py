import math

while True:

    try:
        linha = input()
        if not linha:
            break
        n = int(linha)

        vezes = int(math.log2(n))

        print(vezes)

    except EOFError:
        break