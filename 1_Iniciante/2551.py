import sys

def main():
    input_data = sys.stdin.read().split()

    if not input_data:
        return

    iterator = iter(input_data)

    while True:
        try:
            n_str = next(iterator)
            n = int(n_str)

            recorde_atual = 0.0

            for dia in range(1, n + 1):
                t = int(next(iterator))
                d = int(next(iterator))

                velocidade_media = d / t

                if dia == 1 or velocidade_media > recorde_atual:
                    recorde_atual = velocidade_media
                    print(dia)

        except StopIteration:
            break

if __name__ == "__main__":
    main()