e, f, c = map(int, input().split())

vazias = e + f

total_refri = 0

while vazias >= c:
    novos = vazias // c
    total_refri += novos

    vazias = (vazias % c) + novos

print(total_refri)