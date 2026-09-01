n = int(input())

for _ in range(n):

    x, y = map(int, input().split())

    menor = min(x, y)
    maior = max(x, y)

    soma_impares = 0

    for num in range(menor + 1, maior):
        if num % 2 != 0:
            soma_impares += num

    print(soma_impares)