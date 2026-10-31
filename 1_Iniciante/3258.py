import sys
import math
import heapq

def resolver():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = float(input_data[0])
    N = int(input_data[1])
    
    vegetais = [int(x) for x in input_data[2:2+N]]
    
    heap = []
    min_pedaco = float('inf')
    
    for v in vegetais:
        heapq.heappush(heap, (-float(v), v, 1))
        if v < min_pedaco:
            min_pedaco = float(v)
            
    total_cortes = 0
    
    while True:
        neg_max_pedaco, orig_w, pedacos = heapq.heappop(heap)
        max_pedaco = -neg_max_pedaco
        
        if min_pedaco / max_pedaco >= T:
            break
            
        novos_pedacos = pedacos + 1
        total_cortes += 1
        
        novo_tamanho_pedaco = orig_w / novos_pedacos
        
        if novo_tamanho_pedaco < min_pedaco:
            min_pedaco = novo_tamanho_pedaco
            
        heapq.heappush(heap, (-novo_tamanho_pedaco, orig_w, novos_pedacos))
        
    print(total_cortes)

if __name__ == '__main__':
    resolver()
