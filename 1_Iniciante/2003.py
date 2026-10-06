while True:

    try:
        linha = input().strip()

        hora, minuto = linha.split(":")
        hora = int(hora)
        minuto = int(minuto)

        tempo_maximo = (hora * 60) + minuto + 60

        tempo_encontro = 8 * 60

        atraso = tempo_maximo  - tempo_encontro

        if atraso < 0:
            atraso = 0

        print(f"Atraso maximo: {atraso}")

    except EOFError:
        break