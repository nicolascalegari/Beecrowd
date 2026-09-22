imprimir = False

while True:
    try:
        linha = input()

        if "<body>" in linha:
            imprimir = True
            continue

        if "</body>" in linha:
            imprimir = False

        if imprimir:
            print(linha)

    except EOFError:
        break