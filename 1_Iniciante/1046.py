inicio, final = map(int, input().split())

if inicio < final:
    duracao = final - inicio
else:
    duracao = (24 - inicio) + final

print(f"O JOGO DUROU {duracao} HORA(S)")