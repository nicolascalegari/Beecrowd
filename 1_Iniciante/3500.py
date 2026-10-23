while True:

    try:

        numero = input().strip()
        numero_invertido = numero[::-1]

        print(f"Invertido = {int(numero_invertido)}")

    except EOFError:
        break