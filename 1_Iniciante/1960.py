n = int(input())

valores = [900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
ramanos = ["CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
resultado = ""

for i in range(len(valores)):
    while n >= valores[i]:
        resultado += ramanos[i]
        n -= valores[i]

print(resultado)