while True:

    try:
        linha_n = input()
        if not linha_n:
            break
        n = int(linha_n)

        votos = input().split()
        favoraveis = votos.count("1")

        if favoraveis >= (2 * n) / 3:
            print("impeachment")
        else:
            print("acusacao arquivada")

    except EOFError:
        break