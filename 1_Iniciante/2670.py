import sys

def main():
    input_data = sys.stdin.read().split()


    if not input_data:
        return

    a1 = int(input_data[0])
    a2 = int(input_data[1])
    a3 = int(input_data[2])

    tempo_no_andar1 = (a2 * 2) + (a3 * 4)
    tempo_no_andar2 = (a1 * 2) + (a3 * 2)
    tempo_no_andar3 = (a1 * 4) + (a2 * 2)

    menor_tempo = min(tempo_no_andar1, tempo_no_andar2, tempo_no_andar3)

    print(menor_tempo)

if __name__ == '__main__':
    main()