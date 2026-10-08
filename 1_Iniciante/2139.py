dias_por_mes = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dia_natal = 360 # Soma dos dias ate o natal

while True:
    try:
        mes, dia = map(int, input().split())
        dias_passados = sum(dias_por_mes[:mes]) + dia

        if dias_passados == dia_natal:
            print("E natal!")
        elif dias_passados == dia_natal - 1:
            print("E vespera de natal!")
        elif dias_passados > dia_natal:
            print("Ja passou!")
        else:
            dias_faltantes = dia_natal - dias_passados
            print(f"Faltam {dias_faltantes} dias para o natal!")
    except EOFError:
        break
