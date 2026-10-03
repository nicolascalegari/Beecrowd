def main():

    operacao = input().strip()

    soma = 0.0
    elementos_acima = 0

    for linha in range(12):
        for coluna in range(12):
            valor = float(input())

            if linha + coluna < 11:
                soma += valor
                elementos_acima += 1

    if operacao == 'S':
        print(f"{soma:.1f}")
    elif operacao == 'M':
        media = soma / elementos_acima
        print(f"{media:.1f}")

if __name__ == '__main__':
    main()