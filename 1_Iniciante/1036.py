import math # Necessario para usar math.sqrt

a, b, c = map(float, input().split())

# Calculo do delta
delta = b ** 2 - 4 * a * c

# Divisão por zero ou delta < 0
if a == 0 or delta < 0:
    print("Impossivel calcular")
else:
    # Calculo das raizes
    r1 = (-b + math.sqrt(delta)) / (2 * a)
    r2 = (-b - math.sqrt(delta)) / (2 * a)

    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")