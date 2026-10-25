vence = {
    "pedra": "tesoura",
    "papel": "pedra",
    "tesoura": "papel"
}

while True:
    try:
        linha = input()
        if not linha:
            break

        dodo, leo, pepper = linha.split()

        if vence[dodo] == leo and vence[dodo] == pepper:
            print("Os atributos dos monstros vao ser inteligencia, sabedoria...")
        elif vence[leo] == dodo and vence[leo] == pepper:
            print("Iron Maiden's gonna get you, no matter how far!")
        elif vence[pepper] == dodo and vence[pepper] == leo:
            print("Urano perdeu algo muito precioso...")
        else:
            print("Putz vei, o Leo ta demorando muito pra jogar...")

    except EOFError:
        break