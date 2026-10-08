n = int(input())

for _ in range(n):
    jogador1 = input().strip()
    jogador2 = input().strip()

    # Casos de empate
    if jogador1 == "ataque" and jogador2 == "ataque":
        print("Aniquilacao mutua")
    elif jogador1 == "pedra" and jogador2 == "pedra":
        print("Sem ganhador")
    elif jogador1 == "papel" and jogador2 == "papel":
        print("Ambos venceram")

    # Caso onde jogador 1 vence
    elif jogador1 == "ataque" and (jogador2 == "pedra" or jogador2 == "papel"):
        print("Jogador 1 venceu")
    elif jogador1 == "pedra" and jogador2 == "papel":
        print("Jogador 1 venceu")

    # Caso onde jogador 2 vence
    elif jogador2 == "ataque" and (jogador1 == "pedra" or jogador1 == "papel"):
        print("Jogador 2 venceu")
    elif jogador2 == "pedra" and jogador1 == "papel":
        print("Jogador 2 venceu")