import sys

def merge_sort(arr, l, r):
    if l >= r:
        return 0
    mid = (l + r) // 2
    cost = 0
    cost += merge_sort(arr, l, mid)
    cost += merge_sort(arr, mid + 1, r)
    cost += merge(arr, l, mid, r)
    return cost

def merge(arr, l, mid, r):
    left_copy = arr[l:mid + 1]
    right_copy = arr[mid + 1:r + 1]
    
    i = 0
    j = 0
    k = l
    cost = 0
    
    sum_left_remaining = sum(item[1] for item in left_copy)
    count_left_remaining = len(left_copy)
    
    while i < len(left_copy) and j < len(right_copy):
        # Compara os identificadores (índice 0 da tupla)
        if left_copy[i][0] <= right_copy[j][0]:
            arr[k] = left_copy[i]
            sum_left_remaining -= left_copy[i][1]
            count_left_remaining -= 1
            i += 1
        else:
            arr[k] = right_copy[j]
            # Acumula o custo ponderado das inversões
            cost += count_left_remaining * right_copy[j][1] + sum_left_remaining
            j += 1
        k += 1
        
    while i < len(left_copy):
        arr[k] = left_copy[i]
        i += 1
        k += 1
        
    while j < len(right_copy):
        arr[k] = right_copy[j]
        j += 1
        k += 1
        
    return cost

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    output = []
    
    try:
        while True:
            N = int(next(iterator))
            ids = [int(next(iterator)) for _ in range(N)]
            tempos = [int(next(iterator)) for _ in range(N)]
            
            # Combina os IDs e os tempos em pares (id, tempo)
            packages = list(zip(ids, tempos))
            
            total_cost = merge_sort(packages, 0, N - 1)
            output.append(str(total_cost))
            
    except StopIteration:
        pass
    
    sys.stdout.write('\n'.join(output) + '\n')

if __name__ == '__main__':
    main()