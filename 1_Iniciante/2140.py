def resolver():
    notas = [2, 5, 10, 20, 50, 100]
    combinacoes = set()
    for i in range(len(notas)):
        for j in range(i, len(notas)):
            combinacoes.add(notas[i] + notas[j])

    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break

        troco = m - n

        if troco in combinacoes:
            print("possible")
        else:
            print("impossible")

if __name__ == "__main__":
    resolver()