novo_calculo = 1

while novo_calculo == 1:
    notas_validas = 0
    soma_notas = 0

    while notas_validas < 2:
        nota = float(input())

        if 0.0 <= nota <= 10.0:
            soma_notas += nota
            notas_validas += 1
        else:
            print("nota invalida")

    media = soma_notas / 2
    print(f"media = {media:.2f}")

    while True:
        print("novo calculo (1-sim 2-nao)")
        novo_calculo = int(input())
        if novo_calculo == 1 or novo_calculo == 2:
            break