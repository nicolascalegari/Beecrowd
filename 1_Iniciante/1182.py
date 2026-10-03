def main():

    coluna_alvo = int(input())

    operacao = input().strip()

    soma = 0.0

    for linha in range(12):
        for coluna in range(12):
            valor = float(input())
            if coluna == coluna_alvo:
                soma += valor

    if operacao == 'S':
        print(f"{soma:.1f}")
    elif operacao == 'M':
        media = soma / 12.0
        print(f"{media:.1f}")

if __name__ == "__main__":
    main()