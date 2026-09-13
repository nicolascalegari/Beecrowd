while True:
    try:
        linha = input()
        if not linha.strip():
            continue
        n, meu_id = map(int, linha.split())
        cont = 0

        for _ in range(n):
            id_autor, tipo_jogo = map(int, input().split())

            if id_autor == meu_id and tipo_jogo == 0:
                cont += 1

        print(cont)
    except EOFError:
        break