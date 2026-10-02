s = 0

d = 1

for numerador in range(1, 40, 2):

    s += numerador / d
    d *= 2

print(f"{s:.2f}")