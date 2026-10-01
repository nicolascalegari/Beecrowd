x, y = map(int,input().split())

for i in range(1, y + 1):

    if i % x == 0 or i == y:
        print(i)
    else:
        print(i, end=" ") # end=" " faz o python nao pular a linha, nesse caso apenas coloca um espaço em branco e continua na mesma linha