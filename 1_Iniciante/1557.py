while True:

    n = int(input())

    if n == 0:
        break

    maior = 2 ** (2 * n - 2)
    digitos = len(str(maior))

    for i in range(n):
        linha = []

        for j in range(n):
            valor = 2 ** (i + j) # Valor de cada elemento

            # Formatação
            formatado = str(valor).rjust(digitos)
            linha.append(formatado)

        print(" ".join(linha))

    print()