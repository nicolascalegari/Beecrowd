import sys

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return

    n = int(entrada[0])

    ultizacao_total = 0.0
    posicao = 1

    for _ in range(n):
        c = int(entrada[posicao])
        p = int(entrada[posicao + 1])
        ultizacao_total += c / p
        posicao += 2

    if ultizacao_total <= 1.0:
        print("OK")
    else:
        print("FAIL")

if __name__ == "__main__":
    main()