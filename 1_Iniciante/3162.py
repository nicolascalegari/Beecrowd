import math

def resolver():
    n = int(input())
    aeronaves = []
    for _ in range(n):
        x, y, z = map(int, input().split())
        aeronaves.append((x, y, z))

    for i in range(n):
        menor_distancia = float('inf')
        x1, y1, z1 = aeronaves[i]

        for j in range(n):
            if i == j:
                continue

            x2, y2, z2 = aeronaves[j]
            distancia = math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)

            if distancia < menor_distancia:
                menor_distancia = distancia

        if menor_distancia <= 20:
            print("A")
        elif menor_distancia <= 50:
            print("M")
        else:
            print("B")

if __name__ == '__main__':
    resolver()