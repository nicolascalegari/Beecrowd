import sys
from collections import deque

def resolver():
    # Lê todos os dados da entrada padrão de uma vez só
    dados_entrada = sys.stdin.read().split()
    if not dados_entrada:
        return

    iterador = iter(dados_entrada)
    
    try:
        qtd_ruas = int(next(iterador))
    except StopIteration:
        return

    grafo = {}
    grafo_invertido = {}
    ordem_entrada = []

    # Monta a estrutura do mapa de ruas (grafos)
    for _ in range(qtd_ruas):
        origem = int(next(iterador))
        qtd_conexoes = int(next(iterador))
        
        # Só rastreamos a ordem das ruas reais (id > 0)
        if origem > 0:
            ordem_entrada.append(origem)
            
        if origem not in grafo:
            grafo[origem] = []
        if origem not in grafo_invertido:
            grafo_invertido[origem] = []

        for _ in range(qtd_conexoes):
            destino = int(next(iterador))
            grafo[origem].append(destino)
            
            if destino not in grafo_invertido:
                grafo_invertido[destino] = []
            grafo_invertido[destino].append(origem)

    # 1. Busca para identificar quem consegue chegar ao nó 0 (Para achar as ruas PRESAS)
    consegue_chegar_ao_zero = set()
    fila = deque()
    
    if 0 in grafo_invertido or 0 in grafo:
        consegue_chegar_ao_zero.add(0)
        fila.append(0)
        while fila:
            atual = fila.popleft()
            for vizinho in grafo_invertido.get(atual, []):
                if vizinho not in consegue_chegar_ao_zero:
                    consegue_chegar_ao_zero.add(vizinho)
                    fila.append(vizinho)

    # 2. Busca para identificar quem é alcançável saindo do nó 0 (Para achar as ruas INALCANÇÁVEIS)
    alcancavel_pelo_zero = set()
    fila = deque()
    
    if 0 in grafo or 0 in grafo_invertido:
        alcancavel_pelo_zero.add(0)
        fila.append(0)
        while fila:
            atual = fila.popleft()
            for vizinho in grafo.get(atual, []):
                if vizinho not in alcancavel_pelo_zero:
                    alcancavel_pelo_zero.add(vizinho)
                    fila.append(vizinho)

    # Identifica os problemas baseando-se na ordem em que as ruas foram lidas
    ruas_presas = [rua for rua in ordem_entrada if rua not in consegue_chegar_ao_zero]
    ruas_inalcancaveis = [rua for rua in ordem_entrada if rua not in alcancavel_pelo_zero]

    # Exibe as mensagens conforme a especificação do problema
    if not ruas_presas and not ruas_inalcancaveis:
        print("NO PROBLEMS")
    else:
        for rua in ruas_presas:
            print(f"TRAPPED {rua}")
        for rua in ruas_inalcancaveis:
            print(f"UNREACHABLE {rua}")

if __name__ == '__main__':
    resolver()    