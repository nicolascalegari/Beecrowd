n = int(input())

t = list(map(int, input().split()))

menor_valor = min(t)

# posicao menor + 1 pq inicia no indice 0
posicao_menor = t.index(menor_valor) + 1

print(posicao_menor)