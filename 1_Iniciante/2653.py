joias = set()

while True:

    try:

        linha = input()

        joias.add(linha)

    except EOFError:
        break

print(len(joias))