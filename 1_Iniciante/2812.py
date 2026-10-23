casos = int(input())

for _ in range(casos):
    n = int(input())
    valores = list(map(int, input().split()))

    impares = [x for x in valores if x % 2 != 0]

    impares.sort()

    resultado = []
    esquerda = 0
    direita = len(impares) - 1

    while esquerda <= direita:
        if esquerda == direita:
            resultado.append(str(impares[direita]))
        else:
            resultado.append(str(impares[direita]))
            resultado.append(str(impares[esquerda]))

        direita -= 1
        esquerda += 1

    print(" ".join(resultado))