lista_nums = []
maior = float('-inf')
idx = 0

for i in range(100):

    lista_nums.append(int(input()))
    if lista_nums[i] > maior:
        maior = lista_nums[i]
        idx = i

print(maior)
print(idx+1)