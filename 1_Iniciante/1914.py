n = int(input())

for _ in range(n):

    nome1, escolha1, nome2, escolha2 = input().split()

    num1, num2 = map(int, input().split())

    resultado = "PAR" if (num1 + num2) % 2 == 0 else "IMPAR"

    if escolha1 == resultado:
        print(nome1)
    else:
        print(nome2)