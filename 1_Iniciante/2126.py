caso = 1

while True:
    try:
        subsequencia = input().strip()
        string_completa = input().strip()
        print(f"Caso #{caso}:")

        qtd = string_completa.count(subsequencia)

        if qtd == 0:
            print("Nao existe subsequencia")
        else:
            print(f"Qtd.Subsequencias: {qtd}")

            posicao = string_completa.rfind(subsequencia) + 1
            print(f"Pos: {posicao}")

        print()
        caso += 1

    except EOFError:
        break