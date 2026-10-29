def main():
    while True:
        try:

            linha1 = input().split()
            if not linha1:
                break
            
            H = float(linha1[0])
            M = float(linha1[1])
            
            valores = [float(v) for v in input().split()]
            
            QT = len(valores)
            if QT <= 1:
                continue
            
            media = sum(valores) / QT
            
            soma_quadrados = sum((x - media) ** 2 for x in valores)
            
            desvio_padrao = (soma_quadrados / (QT - 1)) ** 0.5
            
            print(f"{desvio_padrao:.5f}")
            
        except EOFError:
            break

if __name__ == "__main__":
    main()