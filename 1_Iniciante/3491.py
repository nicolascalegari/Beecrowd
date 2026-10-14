import sys

def main():
    entrada = sys.stdin.read().split()

    for token in entrada:
        if token:
            n = int(token)
            letra = chr(97 + (n - 1))
            print(letra)

if __name__ == "__main__":
    main()