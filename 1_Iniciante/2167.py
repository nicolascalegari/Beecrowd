def resolver():
    n = int(input())
    velocidades = list(map(int,input().split()))
    posicao_queda = 0
    for i in range(1, n):
        if velocidades[i] < velocidades[i - 1]:
            posicao_queda = i + 1
            break
    print(posicao_queda)

if __name__ == "__main__":
    resolver()