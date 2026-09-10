n = int(input())
soma = 0

for _ in range(n):

    produto, qtd = map(int,input().split())

    if produto == 1001:
        soma += qtd * 1.50
    elif produto == 1002:
        soma += qtd * 2.50
    elif produto == 1003:
        soma += qtd * 3.50
    elif produto == 1004:
        soma += qtd * 4.50
    elif produto == 1005:
        soma += qtd * 5.50

print(f"{soma:.2f}")