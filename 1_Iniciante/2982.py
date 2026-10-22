import sys

def main():

    linha_n = sys.stdin.readline()
    if not linha_n:
        return
    n = int(linha_n.strip())
    
    total_verba = 0
    total_gastos = 0
    
    for _ in range(n):
        evento = sys.stdin.readline().split()
        if not evento:
            continue
        tipo = evento[0]
        valor = int(evento[1])
        
        if tipo == 'V':
            total_verba += valor
        elif tipo == 'G':
            total_gastos += valor
            
    if total_verba >= total_gastos:
        print("A greve vai parar.")
    else:
        print("NAO VAI TER CORTE, VAI TER LUTA!")

if __name__ == '__main__':
    main()