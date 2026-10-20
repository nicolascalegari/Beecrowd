import sys

def main():
    input_data = sys.stdin.read().split()

    if not input_data:
        return

    n = int(input_data[0])
    k = int(input_data[1])

    notas = []

    for i in range(2, 2 + n):
        notas.append(int(input_data[i]))


    notas.sort(reverse=True)

    classificados = k

    while classificados < n and notas[classificados] == notas[k - 1]:
        classificados += 1

    print(classificados)

if __name__ == '__main__':
    main()