h, e, a, o, w, x = map(int, input().split())

bom = h + e + a
mal = o + w

if bom >= mal:
    print("Middle-earth is safe.")
else:
    bom += x
    if bom >= mal:
        print("Middle-earth is safe.")
    else:
        print("Sauron has returned.")