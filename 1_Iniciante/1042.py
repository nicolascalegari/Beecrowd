a, b, c = map(int, input().split())

#Lista
valores_originais = [a, b, c]

#Nova lista ordena crescente
valores_ordenados = sorted(valores_originais)

#Imprime valor crescente
for valor in valores_ordenados:
    print(valor)

print()

#Imprime valor original
for valor in valores_originais:
    print(valor)