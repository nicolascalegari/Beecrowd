import sys

def resolver():

    LIMITE = 10000000
    
    eh_primo = bytearray([1]) * (LIMITE + 1)
    eh_primo[0] = eh_primo[1] = 0
    
    # Corta os múltiplos de 2
    for i in range(4, LIMITE + 1, 2):
        eh_primo[i] = 0
        
    for i in range(3, int(LIMITE**0.5) + 1, 2):
        if eh_primo[i]:
            for j in range(i * i, LIMITE + 1, i * 2):
                eh_primo[j] = 0

    pref = [0] * (LIMITE + 1)
    acumulado = 0
    for i in range(LIMITE + 1):
        if eh_primo[i]:
            acumulado += 1
        pref[i] = acumulado

    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    
    resultados = []
    idx = 1
    for _ in range(n):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        idx += 2
        
        total_no_intervalo = pref[b] - pref[a - 1]
        resultados.append(str(total_no_intervalo))
        
    sys.stdout.write('\n'.join(resultados) + '\n')

if __name__ == '__main__':
    resolver()
