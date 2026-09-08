a, b = map(int,input().split())

# trio
if a == b:
    print(a)
# se as cartas forem != a melhor carta é de maior valor
elif a > b:
    print(a)
else: print(b)