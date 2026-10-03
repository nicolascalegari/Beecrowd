def main():

    pares = []
    impares = []

    for _ in range(15):
        num = int(input())

        if num % 2 == 0:
            pares.append(num)

            if len(pares) == 5:
                for i, v in enumerate(pares):
                    print(f"par[{i}] = {v}")
                pares = []
        else:
            impares.append(num)

            if len(impares) == 5:
                for i, v in enumerate(impares):
                    print(f"impar[{i}] = {v}")
                impares = []

    for i, v in enumerate(impares):
        print(f"impar[{i}] = {v}")

    for i, v in enumerate(pares):
        print(f"par[{i}] = {v}")

if __name__ == '__main__':
    main()