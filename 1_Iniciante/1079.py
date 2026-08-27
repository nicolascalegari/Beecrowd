n = int(input())

while n != 0:
    a, b, c = map(float, input().split())
    print(f"{(a * 2 + b * 3 + c * 5) / 10:.1f}")
    n -= 1