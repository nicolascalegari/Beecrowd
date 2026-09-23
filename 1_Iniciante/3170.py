bolinhas = int(input())
galhos = int(input())

if galhos % 2 != 0:
    galhos -= 1

bolinhas_ideal = galhos / 2

if bolinhas >= bolinhas_ideal:
    print("Amelia tem todas bolinhas!")
else:
    faltam = bolinhas_ideal - bolinhas
    print(f"Faltam {faltam:.0f} bolinha(s)")