n = int(input())

for _ in range(n):

    x = int(input())

    if x <= 1:
        print(f"{x} nao eh primo")
        continue

    eh_primo = True

    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            eh_primo = False
            break

    if eh_primo:
        print(f"{x} eh primo")
    else:
        print(f"{x} nao eh primo")