n = int(input())

for _ in range(n):

    x = int(input())

    soma_div = 0

    for i in range(1, x):

        if x % i == 0:
            soma_div += i

    if soma_div == x:
        print(f"{x} eh perfeito")
    else:
        print(f"{x} nao eh perfeito")