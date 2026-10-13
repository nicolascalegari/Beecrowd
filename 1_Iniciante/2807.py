n = int(input())

fib = [1, 1]

while len(fib) < n:
    proximo = fib[-1] + fib[-2]
    fib.append(proximo)

sequencia = fib[:n]

sequencia_invertida = sequencia[::-1]

print(*(sequencia_invertida))