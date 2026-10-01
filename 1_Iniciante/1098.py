for i_int in range(0, 21, 2):

    i = i_int / 10

    for j_base in range(10, 40, 10):

        j = (j_base + i_int) / 10

        if i_int % 10 == 0:
            print(f"I={int(i)} J={int(j)}")
            
        else:
            print(f"I={i:.1f} J={j:.1f}")
