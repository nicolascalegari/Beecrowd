n = int(input())

for _ in range(n):

    h, m, o = map(int, input().split())

    horario = f"{h:02d}:{m:02d}"

    if o == 1:
        print(f"{horario} - A porta abriu!")
    else:
        print(f"{horario} - A porta fechou!")