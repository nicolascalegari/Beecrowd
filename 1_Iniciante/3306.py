import math

def main():
    entrada = open(0).read().split()
    
    if not entrada:
        return

    ponteiro = 0
    n = int(entrada[ponteiro])
    q = int(entrada[ponteiro + 1])
    ponteiro += 2
    
    vetor = [0] + [int(x) for x in entrada[ponteiro:ponteiro + n]]
    ponteiro += n
    
    for _ in range(q):
        if ponteiro >= len(entrada):
            break
            
        tipo = int(entrada[ponteiro])
        ponteiro += 1
        
        if tipo not in (1, 2):
            continue
            
        a = int(entrada[ponteiro])
        b = int(entrada[ponteiro + 1])
        ponteiro += 2
        
        if a > b:
            a, b = b, a
            
        if tipo == 1:
            v = int(entrada[ponteiro])
            ponteiro += 1
            for i in range(a, b + 1):
                vetor[i] += v
                
        elif tipo == 2:
            mdc_atual = vetor[a]
            for i in range(a + 1, b + 1):
                mdc_atual = math.gcd(mdc_atual, vetor[i])
                if mdc_atual == 1:
                    break
            print(mdc_atual)

if __name__ == '__main__':
    main()