n = int(input())

lista = list(map(int, input().split()))

mult_2 = 0
mult_3 = 0
mult_4 = 0
mult_5 = 0

for num in lista:

    if num % 2 == 0:
        mult_2 += 1
    if num % 3 == 0:
        mult_3 += 1
    if num % 4 == 0:
        mult_4 += 1
    if num % 5 == 0:
        mult_5 += 1

print(f"{mult_2} Multiplo(s) de 2")
print(f"{mult_3} Multiplo(s) de 3")
print(f"{mult_4} Multiplo(s) de 4")
print(f"{mult_5} Multiplo(s) de 5")