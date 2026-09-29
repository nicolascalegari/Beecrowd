import sys
from functools import cache

# Define as 6 direções de movimento no hexagono
direcoes = [(0,1),(1,0),(1,-1),(0,-1),(-1,0),(-1,1)]

@cache
def contar_caminhos(passos, x, y):
    # Se os passos acabaram, verifica se voltou para a origem (0,0)
    if passos == 0:
        return 1 if (x == 0 and y == 0) else 0

    total = 0

    # Tenta andar para as 6 direções
    for dx, dy in direcoes:
        total += contar_caminhos(passos - 1, x + dx, y + dy)
    return total

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return

    casos = int(entrada[0])
    for i in range(1, casos + 1):
        n = int(entrada[i])
        # Começa com N passos na origem (0,0)
        print(contar_caminhos(n, 0, 0))

if __name__ == '__main__':
    main()