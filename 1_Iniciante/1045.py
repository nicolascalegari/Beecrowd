#Leitura de valores em uma lista
valores = list(map(float, input().split()))

#Ordenação dos valores em ordem descrescente
valores.sort(reverse = True)
a, b, c = valores

#Condições
if a >= (b + c):
    print("NAO FORMA TRIANGULO")
else:
    if (a**2) == (b**2 + c**2):
        print("TRIANGULO RETANGULO")
    elif (a**2) > (b**2 + c**2):
        print("TRIANGULO OBTUSANGULO")
    elif (a**2) < (b**2 + c**2):
        print("TRIANGULO ACUTANGULO")

    #Segunda condição
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or b == c or a == c:
        print("TRIANGULO ISOSCELES")