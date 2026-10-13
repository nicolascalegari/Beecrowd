while True:
    try:
        linha = input().split()
        if not linha:
            break
        
        n = int(linha[0])
        m = int(linha[1])
        
        # Leitura da matriz de pãezinhos de queijo
        matriz = []
        for _ in range(n):
            matriz.append([int(x) for x in input().split()])
            
        # Processamento e impressão do tabuleiro final
        for i in range(n):
            linha_resultado = []
            for j in range(m):
                # Se a célula atual contém um pãozinho de queijo, o valor é 9
                if matriz[i][j] == 1:
                    linha_resultado.append("9")
                else:
                    # Contador de pãezinhos vizinhos nas 4 direções adjacentes
                    paes_vizinhos = 0
                    
                    # Acima
                    if i > 0 and matriz[i-1][j] == 1:
                        paes_vizinhos += 1
                    # Abaixo
                    if i < n - 1 and matriz[i+1][j] == 1:
                        paes_vizinhos += 1
                    # À esquerda
                    if j > 0 and matriz[i][j-1] == 1:
                        paes_vizinhos += 1
                    # À direita
                    if j < m - 1 and matriz[i][j+1] == 1:
                        paes_vizinhos += 1
                        
                    linha_resultado.append(str(paes_vizinhos))
            
            print("".join(linha_resultado))
            
    except EOFError:
        break
