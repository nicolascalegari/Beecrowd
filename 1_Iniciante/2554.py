import sys

def main():
    input_data = sys.stdin.read().split()

    if not input_data:
        return

    iterator = iter(input_data)

    while True:
        try:
            n = int(next(iterator))
            d = int(next(iterator))

            data_escolhida = None

            for _ in range(d):
                data_atual = next(iterator)
                presencas = [int(next(iterator)) for _ in range(n)]

                if sum(presencas) == n and data_escolhida is None:
                    data_escolhida = data_atual

            if data_escolhida is not None:
                print(data_escolhida)
            else:
                print("Pizza antes de FdI")

        except StopIteration:
            break
if __name__ == '__main__':
    main()