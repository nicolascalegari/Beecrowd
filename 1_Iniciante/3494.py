s = input().strip()
t = input().strip()

custo_total = 0

for i in range(len(s)):
    diferenca = abs(ord(s[i]) - ord(t[i]))
    custo = min(diferenca, 26 - diferenca)
    custo_total += custo

print(custo_total)