import sys

def main():
    input_data = sys.stdin.read().split()

    for item in input_data:
        x = int(item)

        if x == 0:
            break

        print(" ".join(str(i) for i in range(1, x + 1)))

if __name__ == '__main__':
    main()