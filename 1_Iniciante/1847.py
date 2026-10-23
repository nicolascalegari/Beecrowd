a, b, c = map(int, input().split())

# Se a temp desceu do primeiro para o segundo dia
if a > b:
    # Subiu ou permaneceu constante do segundo para o terceiro
    if b <= c:
        print(":)")
    # Desceu no segundo para o terceiro, mas desceu menos do que do primeiro para o segundo
    elif b > c and (a - b) > (b - c):
        print(":)")
    # Desceu do segundo para o terceiro mas desceu mais ou igual do que do primeiro para segundo
    else:
        print(":(")

# Se a temp subiu do primeiro para o segundo
elif a < b:
    # Desceu ou permaneceu constante do segundo para o terceiro
    if b >= c:
        print(":(")
    # Subiu do segundo para o terceiro mas subiu menos do que do primeiro para o segundo
    elif b < c and (b - a) > (c - b):
        print(":(")
    # Subiu do segundo para o terceiro, mas subiu mais ou igual do que do primeiro para o segundo
    else:
        print(":)")

# A temp permaneceu constante do primeiro para o segundo dia
else:
    # Subiu do segundo para o terceiro
    if b < c:
        print(":)")
    # Desceu ou permanceu constante do segundo para o terceiro
    else:
        print(":(")