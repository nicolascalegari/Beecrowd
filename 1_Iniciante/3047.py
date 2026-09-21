idade_mae = int(input())
idade_filho_1 = int(input())
idade_filho_2 = int(input())
idade_filho_3 = idade_mae - (idade_filho_1 + idade_filho_2)

print(max(idade_filho_1, idade_filho_2, idade_filho_3))