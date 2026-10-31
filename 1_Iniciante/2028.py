import sys

def resolver():

    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    caso = 1
    for num_str in input_data:
        N = int(num_str)
        
        sequencia = [0]
        for i in range(1, N + 1):
            sequencia.extend([i] * i)
        
        total_elementos = len(sequencia)
        
        palavra_numero = "numero" if total_elementos == 1 else "numeros"
        
        print(f"Caso {caso}: {total_elementos} {palavra_numero}")
        
        print(*(sequencia))
        
        print()
        
        caso += 1

if __name__ == '__main__':
    resolver()
