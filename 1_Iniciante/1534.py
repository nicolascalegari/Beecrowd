while True:

    try:

        n = int(input())

        for i in range(n):
            linha = []
            for j in range(n):
                if i + j == n - 1:
                    linha.append("2")
                elif i == j:
                    linha.append("1")
                else:
                    linha.append("3")
            print("".join(linha))

    except EOFError:
        
        break