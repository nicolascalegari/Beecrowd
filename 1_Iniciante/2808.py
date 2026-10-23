pos_inicial, pos_final = input().split()

x1 = ord(pos_inicial[0]) - 96
y1 = int(pos_inicial[1]) 

x2 = ord(pos_final[0]) - 96
y2 = int(pos_final[1])

diff_x = abs(x1 - x2)
diff_y = abs(y1 - y2)

if (diff_x == 2 and diff_y == 1) or (diff_x == 1 and diff_y == 2):
    print("VALIDO")
else:
    print("INVALIDO")