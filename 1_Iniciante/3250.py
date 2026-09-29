from collections import deque

def resolver_elevador():
    
    f, s, g, u, d = map(int, input().split())
    
    # Se já está no andar de destino, zero botões precisam ser pressionados
    if s == g:
        print(0)
        return

    # Lista para rastrear os andares já visitados (1 até f)
    visitados = [False] * (f + 1)
    
    # Fila para a BFS armazenando tuplas: (andar_atual, cliques_de_botao)
    fila = deque([(s, 0)])
    visitados[s] = True
    
    while fila:
        andar_atual, cliques = fila.popleft()
        
        # Verifica se chegou ao destino
        if andar_atual == g:
            print(cliques)
            return
        
        # Subir
        andar_sobe = andar_atual + u
        if andar_sobe <= f and not visitados[andar_sobe]:
            visitados[andar_sobe] = True
            fila.append((andar_sobe, cliques + 1))
            
        # Descer
        andar_desce = andar_atual - d
        if andar_desce >= 1 and not visitados[andar_desce]:
            visitados[andar_desce] = True
            fila.append((andar_desce, cliques + 1))
            
    # Se a fila esvaziar e não encontrar o destino, é impossível chegar lá
    print("use the stairs")

if __name__ == "__main__":
    resolver_elevador()
