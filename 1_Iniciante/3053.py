N = int(input())

posicao = input().strip()

for _ in range(N):
    movimento = int(input())

    if movimento == 1:
        if posicao == 'A':
            posicao = 'B'
        elif posicao == 'B':
            posicao = 'A'

    elif movimento == 2:
        if posicao == 'B':
            posicao = 'C'
        elif posicao == 'C':
            posicao = 'B'

    elif movimento == 3:
        if posicao == 'A':
            posicao = 'C'
        elif posicao == 'C':
            posicao = 'A'

print(posicao)