p, j1, j2, r, a = map(int, input().split())

soma = j1 + j2

resultado = 1 if soma % 2 == 0 else 0

if r == 1:
    if a == 1:
        print("Jogador 2 ganha!")
    else:
        print("Jogador 1 ganha!")

else:
    if a == 1:
        print("Jogador 1 ganha!")
    else:
        if p == resultado:
            print("Jogador 1 ganha!")
        else:
            print("Jogador 2 ganha!")