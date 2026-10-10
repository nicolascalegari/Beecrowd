while True:

    try:

        alfabeto = input()

        n = int(input())

        posicoes = list(map(int, input().split()))

        mensagem = ""

        for p in posicoes:
            mensagem += alfabeto[p - 1]

        print(mensagem)

    except EOFError:
        break