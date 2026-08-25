par = 0
imp = 0
pos = 0
neg = 0

i = 0

while i < 5:
    val = int(input())

    if val % 2 == 0:
        par += 1
    else:
        imp += 1

    if val > 0:
        pos += 1
    elif val < 0:
        neg += 1

    i += 1

print(f"{par} valor(es) par(es)")
print(f"{imp} valor(es) impar(es)")
print(f"{pos} valor(es) positivo(s)")
print(f"{neg} valor(es) negativo(s)")