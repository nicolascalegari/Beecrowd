import math

while True:
    try:
        valores = input().split()
        if not valores:
            break

        xf = int(valores[0])
        yf = int(valores[1])
        xi = int(valores[2])
        yi = int(valores[3])
        v = int(valores[4])
        r1 = int(valores[5])
        r2 = int(valores[6])

        distancia_inicial = math.sqrt((xi - xf)**2 + (yi - yf)**2)
        distancia_final = distancia_inicial + (v * 1.5)
        alcance_maximo = r1 + r2

        if distancia_final <= alcance_maximo:
            print("Y")
        else:
            print("N")

    except EOFError:
        break