a = []

for _ in range(100):
    a.append(float(input()))

for i in range(100):
    if a[i] <= 10.0:
        print(f"A[{i}] = {a[i]:.1f}")