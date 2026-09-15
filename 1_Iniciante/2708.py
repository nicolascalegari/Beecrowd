total_turistas = 0
total_jipes = 0

while True:
    entrada = input().split()

    acao = entrada[0]
    if acao == "ABEND":
        break

    qtd_turistas = int(entrada[1])

    if acao == "SALIDA":
        total_turistas += qtd_turistas
        total_jipes += 1

    elif acao == "VUELTA":
        total_turistas -=  qtd_turistas
        total_jipes -= 1

print(total_turistas)
print(total_jipes)