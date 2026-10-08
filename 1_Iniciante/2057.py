s, t, f = map(int, input().split())

hora_chegada = s + t + f

if hora_chegada >= 24:
    hora_chegada = hora_chegada - 24
elif hora_chegada < 0:
    hora_chegada = hora_chegada + 24

print(hora_chegada)