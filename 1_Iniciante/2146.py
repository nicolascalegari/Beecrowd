while True:

    try:

        entrada = int(input())

        print(f"{entrada - 1}")

    except EOFError:
        break