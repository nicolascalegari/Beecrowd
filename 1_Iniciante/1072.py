teste = int(input())

i = 0
dentro = 0
fora = 0

while i < teste:
    num = int(input())
    if num >= 10 and num <= 20:
        dentro += 1
    else:
        fora += 1
    i += 1

print(f"{dentro} in")
print(f"{fora} out")