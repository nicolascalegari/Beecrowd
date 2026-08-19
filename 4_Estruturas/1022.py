from math import gcd
n = int(input())

for _ in range(n):
    entrada = input().split()

    # mapeia as entradas
    n1 = int(entrada[0])
    d1 = int(entrada[2])
    op = entrada[3]
    n2 = int(entrada[4])
    d2 = int(entrada[6])

    if op == '+':
        num = n1 * d2 + n2 *d1
        den = d1 *d2
    elif op == '-':
        num = n1 * d2 - n2 * d1
        den = d1 * d2
    elif op == '*':
        num = n1 * n2
        den = d1 * d2
    else:
        num = n1 * d2
        den = n2 * d1

    # função gcd (maximo divisor comum)
    divisor_comum = gcd(num, den)
    num_simplificado = num // divisor_comum
    den_simplificado = den // divisor_comum

    print(f"{num}/{den} = {num_simplificado}/{den_simplificado}")