x = []

for _ in range(10):
    y = int(input())
    x.append(y)

for i in range(len(x)):

    if x[i] <= 0:
        x[i] = 1

for i in range(len(x)):
    print(f"X[{i}] = {x[i]}")