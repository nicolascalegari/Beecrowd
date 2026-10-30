import re

teste = 1

while True:
    m = int(input())
    if m == 0:
        break

    expressao = input().strip()

    numeros = list(map(int, re.findall(r'\d+', expressao)))
    sinais = re.findall(r'[+-]', expressao)

    resultado = numeros[0]

    for i in range(len(sinais)):
        if sinais[i] == '+':
            resultado += numeros[i + 1]
        else:
            resultado -= numeros[i + 1]

    print(f"Teste {teste}")
    print(resultado)
    print()

    teste += 1