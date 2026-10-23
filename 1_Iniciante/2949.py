n = int(input())

anoes = 0
elfos = 0
humanos = 0
magos = 0
hobbits = 0

for _ in range(n):
    dados = input().split()
    tipo = dados[1]

    if tipo == 'A':
        anoes += 1
    elif tipo == 'E':
        elfos += 1
    elif tipo == 'H':
        humanos += 1
    elif tipo == 'M':
        magos += 1
    elif tipo == 'X':
        hobbits += 1

print(f"{hobbits} Hobbit(s)")
print(f"{humanos} Humano(s)")
print(f"{elfos} Elfo(s)")
print(f"{anoes} Anao(oes)")
print(f"{magos} Mago(s)")