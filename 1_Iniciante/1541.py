while True:
    entrada = input().split()

    if entrada[0] == '0':
        break

    A = int(entrada[0])
    B = int(entrada[1])
    C = int(entrada[2])

    area_casa = A * B

    area_terreno_necessaria = (area_casa * 100) / C

    lado_terreno = int(area_terreno_necessaria ** 0.5)

    print(lado_terreno)