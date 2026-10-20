import sys

def main():
    entradas = sys.stdin.read().split()
    for valor in entradas:
        p = int(valor)

        if p == -1:
            break

        if p == 0:
            print(0)
        else:
            print(p - 1)

if __name__ == '__main__':
    main()