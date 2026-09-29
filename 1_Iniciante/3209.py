n = int(input())

for _ in range(n):

    dados = [int(x) for x in input().split()]

    # Numero de reguas
    k = dados[0]

    # O restante dos numeros sao as tomas de cada regua
    # Do indice 1 ate o final
    reguas = dados[1:]

    total = sum(reguas) - (k - 1) # k -1 tira a ultima regua dessa conta

    print(total)