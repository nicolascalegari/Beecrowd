import sys

def main():

    entrada = sys.stdin.read().split()
    if not entrada:
        return
    k = int(entrada[0])
    
    fib1 = 1
    fib2 = 2
    
    contador_fibonot = 0
    ultimo_fibonot = 0
    
    while contador_fibonot < k:
        proximo_fib = fib1 + fib2
        
        elementos_omitidos = proximo_fib - fib2 - 1
        
        if contador_fibonot + elementos_omitidos >= k:
            posicao_na_lacuna = k - contador_fibonot
            ultimo_fibonot = fib2 + posicao_na_lacuna
            break
        else:
            contador_fibonot += elementos_omitidos
            
        fib1 = fib2
        fib2 = proximo_fib

    print(ultimo_fibonot)

if __name__ == '__main__':
    main()
