n = int(input())

for _ in range(n):

    nome, forca = map(str, input().split())

    if nome == "Thor":
        print("Y")
    else:
        print("N")