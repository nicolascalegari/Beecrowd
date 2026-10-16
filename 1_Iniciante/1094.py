def resolver():
    n = int(input())

    total_coelhos = 0
    total_ratos = 0
    total_sapos = 0

    for _ in range(n):
        linha = input().split()
        quantidade = int(linha[0])
        tipo = linha[1]

        if tipo == 'C':
            total_coelhos += quantidade
        elif tipo == 'R':
            total_ratos += quantidade
        elif tipo == 'S':
            total_sapos += quantidade

    total_geral = total_coelhos + total_sapos + total_ratos

    pct_coelhos = (total_coelhos / total_geral) * 100
    pct_ratos = (total_ratos / total_geral) * 100
    pct_sapos = (total_sapos / total_geral) * 100

    print(f"Total: {total_geral} cobais")
    print(f"Total de coelhos: {total_coelhos}")
    print(f"Total de ratos: {total_ratos}")
    print(f"Total de sapos: {total_sapos}")
    print(f"Percentual de coelhos: {pct_coelhos:.2f} %")
    print(f"Percentural de ratos: {pct_ratos:.2f} %")
    print(f"Percentural de sapos: {pct_sapos:.2f} %")

if __name__ == '__main__':
    resolver()