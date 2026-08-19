a, b, c = map(int, input().split())
maiorab = (a + b + abs(a - b)) / 2
maiorabc = (maiorab+ c + abs(maiorab - c)) / 2
print(f"{maiorabc:.0f} eh o maior")