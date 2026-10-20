import sys

def main():

    input_data = sys.stdin.read().split()

    if not input_data:
        return

    iterator = iter(input_data)

    while True:
        try:
            m_str = next(iterator)
            m = int(m_str)

            soma_produtos = 0
            soma_cargas = 0

            for _ in range(m):
                n = int(next(iterator))
                c = int(next(iterator))

                soma_produtos += n * c
                soma_cargas += c

            ira = soma_produtos / (soma_cargas * 100)

            print(f"{ira:.4f}")

        except StopIteration:
            break

if __name__ == "__main__":
    main()