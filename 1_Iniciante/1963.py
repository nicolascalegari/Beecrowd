preco_antigo, preco_novo = map(float, input().split())

aumento = preco_novo - preco_antigo

porcentagem = (aumento / preco_antigo) * 100

print(f"{porcentagem:.2f}%")