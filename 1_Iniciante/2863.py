import sys

def main():
    linhas = sys.stdin.read().split()
    if not linhas:
        return

    posicao = 0
    total_linhas = len(linhas)

    while posicao < total_linhas:
        n = int(linhas[posicao])
        posicao += 1    
        menor_tempo = float(linhas[posicao])
        posicao += 1

        for _ in range(n - 1):
            tempo_atual = float(linhas[posicao])
            if tempo_atual < menor_tempo:
                menor_tempo = tempo_atual
            posicao += 1

        print(menor_tempo)

if __name__ == '__main__':
    main()