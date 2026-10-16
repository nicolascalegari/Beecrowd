import sys

def resolver():

    input_data = sys.stdin.read().split()

    if not input_data:
        return

    a = int(input_data[0])
    p = int(input_data[1])

    tigres = (p - 2 * a) // 2
    gansos = a - tigres

    print(tigres)
    print(gansos)

if __name__ == '__main__':
    resolver()