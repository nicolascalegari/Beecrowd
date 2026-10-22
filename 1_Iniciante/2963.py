import sys

def main():

    linha_n = sys.stdin.readline()

    if not linha_n:
        return

    n = int(linha_n.strip())

    votos_carlos = int(sys.stdin.readline().strip())

    carlos_ganhou = True

    for _ in range(n - 1):
        votos_concorrente = int(sys.stdin.readline().strip())

        if votos_concorrente > votos_carlos:
            carlos_ganhou = False

    if carlos_ganhou:
        print('S')
    else:
        print('N')

if __name__ == '__main__':
    main()