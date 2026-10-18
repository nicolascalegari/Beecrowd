varetas = list(map(int, input().split()))

varetas.sort()

a, b, c, d = varetas

if a + b > c or b + c > d:
    print('S')
else:
    print('N')