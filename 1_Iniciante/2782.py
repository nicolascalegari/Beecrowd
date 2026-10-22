import sys

def main():

    linha_n = sys.stdin.readline()
    if not linha_n:
        return
    n = int(linha_n.strip())
    
    lista = [int(x) for x in sys.stdin.readline().split()]
    
    if n <= 2:
        print(1)
        return
    
    total_escadinhas = 1
    
    for i in range(2, n):
        diferenca_atual = lista[i] - lista[i-1]
        diferenca_anterior = lista[i-1] - lista[i-2]
        
        if diferenca_atual != diferenca_anterior:
            total_escadinhas += 1
            
    print(total_escadinhas)

if __name__ == '__main__':
    main()