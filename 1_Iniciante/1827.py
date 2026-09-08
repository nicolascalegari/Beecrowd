while True:
    try:

        entrada = input()
        if not entrada.strip():
            continue
        
        n = int(entrada)
        
        inicio_interno = n // 3
        fim_interno = n - inicio_interno
        centro = n // 2

        for i in range(n):
            linha = []
            for j in range(n):

                if i == centro and j == centro:
                    linha.append("4")

                elif inicio_interno <= i < fim_interno and inicio_interno <= j < fim_interno:
                    linha.append("1")

                elif i == j:
                    linha.append("2")

                elif i + j == n - 1:
                    linha.append("3")

                else:
                    linha.append("0")
            
            print("".join(linha))
        
        print()
        
    except EOFError:

        break
