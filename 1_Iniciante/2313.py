lados = list(map(int, input().split()))

lados.sort()

a, b, c = lados[0], lados[1], lados[2]

if a + b > c:
    if a == b == c:
        tipo = "Valido-Equilatero"
    elif a == b or b == c or a == c:
        tipo = "Valido-Isoceles"
    else:
        tipo = "Valido-Escaleno"

    print(tipo)

    if (c ** 2) == (a ** 2 + b ** 2):
        print("Retangulo: S")
    else:
        print("Retangulo: N")

else:
    print("Invalido")