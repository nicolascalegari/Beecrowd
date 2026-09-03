soma = 0
cont = 0
while cont < 2:
    nota = float(input())
    if nota < 0 or nota > 10:
        print("nota invalida")
    else:
        soma += nota
        cont += 1

print(f"media = {soma / cont:.2f}")
