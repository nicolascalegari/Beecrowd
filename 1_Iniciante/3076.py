import sys

for linha in sys.stdin:
    linha = linha.strip()
    if not linha:
        continue

    ano = int(linha)

    seculo = (ano + 99) // 100

    print(seculo)