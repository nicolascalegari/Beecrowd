n = int(input())

fib = [0, 1]

for i in range(2, n):

    proximo = fib[i - 1] + fib[i - 2]
    fib.append(proximo)

resultado = " ".join(map(str, fib[:n]))

print(resultado)