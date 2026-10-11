while True:

    try:

        n, a_min, a_max = map(int, input().split())

        permitidos = 0

        for _ in range(n):

            altura = int(input())

            if a_min <= altura <= a_max:
                permitidos += 1

        print(permitidos)

    except EOFError:
        break