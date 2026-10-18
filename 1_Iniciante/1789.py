import sys

def main():
    linhas = sys.stdin.read().splitlines()

    for i in range(0, len(linhas), 2):
        if not linhas[i]:
            break

        velocidades = list(map(int, linhas[i+1].split()))
        maior_velocidade = max(velocidades)

        if maior_velocidade < 10:
            print(1)
        elif 10 <= maior_velocidade < 20:
            print(2)
        else:
            print(3)

if __name__ == '__main__':
    main()