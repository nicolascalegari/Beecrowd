a, b, c = map(float, input().split())

#Saber se é triangulo
if (a < b + c) and (b < a + c) and (c < a + c):
    perimetro = a + b + c
    print(f"Perimetro = {perimetro:.1f}")
else:
    area = ((a + b) * c) / 2
    print(f"Area = {area:.1f}")