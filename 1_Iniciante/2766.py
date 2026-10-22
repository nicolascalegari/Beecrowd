import sys

def main():
    nomes = []

    for _ in range(10):
        nome = sys.stdin.readline().strip()
        nomes.append(nome)

    print(nomes[2])
    print(nomes[6])
    print(nomes[8])

if __name__ == '__main__':
    main()