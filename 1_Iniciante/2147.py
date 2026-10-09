def resolver():
    c = int(input())
    for _ in range(c):
        palavra = input()
        tempo = len(palavra) * 0.01
        print(f"{tempo:.2f}")
if __name__ == "__main__":
    resolver()