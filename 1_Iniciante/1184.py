def main():

    operacao = input().strip()

    soma = 0.0
    elementos_abaixo = 0

    for linha in range(12):
        for coluna in range(12):
            valor = float(input())

            if linha > coluna:
                soma += valor
                elementos_abaixo += 1

    if operacao == 'S':
        print(f"{soma:.1f}")
    elif operacao == 'M':
        media = soma / elementos_abaixo
        print(f"{media:.1f}")

if __name__ == '__main__':
    main()