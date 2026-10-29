import sys

def main():
    entradas = sys.stdin.read().splitlines()

    idiomas = {
        "esquerda":"ingles",
        "direita":"frances",
        "nenhuma":"portugues",
        "as duas":"caiu",
    }

    for linha in entradas:
        situacao = linha.strip()
        if not situacao:
            continue

        if situacao in idiomas:
            print(idiomas[situacao])

if __name__ == "__main__":
    main()