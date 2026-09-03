valor_1 = int(input())
valor_2 = int(input())

#Garantir o inicio e final
inicio = min(valor_1, valor_2)
fim = max(valor_1, valor_2)

soma = 0

for num in range(inicio, fim + 1):
    if num % 13 != 0:
        soma += num

print(soma)