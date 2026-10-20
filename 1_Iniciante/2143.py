import sys

def main():
    linhas = sys.stdin.read().split()

    if not linhas:
        return

    ponteiro = 0
    while ponteiro < len(linhas):
        t = int(linhas[ponteiro])
        ponteiro += 1

        if t == 0:
            break

        for _ in range(t):
            n = int(linhas[ponteiro])
            ponteiro += 1

            if n % 2 != 0:
                print((n * 2) - 1)
            else:
                print((n * 2) - 2)

if __name__ == '__main__':
    main()