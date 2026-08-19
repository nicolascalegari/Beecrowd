valor = int(input())
print(valor)
aux = valor
notas = [100, 50, 20, 10, 5, 2, 1]
for nota in notas:
    qtd_notas = aux // nota
    aux = aux % nota
    print(f"{qtd_notas} nota(s) de R$ {nota},00")