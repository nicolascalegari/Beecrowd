def resolver():
    n = int(input())
    raiz_5 = 5 ** 0.5
    positvo = (1 + raiz_5) / 2
    negativo = (1 - raiz_5) / 2
    resultado = (positvo ** n - negativo ** n) / raiz_5
    print(f"{resultado:.1f}")
if __name__ == "__main__":
    resolver()