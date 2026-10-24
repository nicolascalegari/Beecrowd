entrada = input().strip()

if entrada == "-0":
    print("-0.0000E+00")
else:
    numero = float(entrada)
    print(f"{numero:+.4E}")