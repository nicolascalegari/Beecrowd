while True:

    try:

        v = float(input())
        d = float(input())

        pi = 3.14

        r = d / 2

        area = pi * (r ** 2)

        altura = v / area

        print(f"ALTURA = {altura:.2f}")
        print(f"AREA = {area:.2f}")

    except EOFError:
        break