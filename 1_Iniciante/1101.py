while True:

    try:

        m, n = map(int, input().split())

        if m <= 0 or n <= 0:
            break

        menor = min(m, n)
        maior = max(m, n)

        soma = 0
        sequencia = []

        for i in range(menor, maior + 1):
            sequencia.append(str(i))
            soma += i

        print(f"{' '.join(sequencia)} Sum={soma}")

    except EOFError:
        break