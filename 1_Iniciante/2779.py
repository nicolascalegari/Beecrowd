total_album = int(input())

compradas = int(input())

# Set mantem apenas elementos unicos
figurinhas_unicas = set()

for _ in range(compradas):
    numero_figurinha = int(input())
    figurinhas_unicas.add(numero_figurinha)

# O que faltam e o total do album menos o tamanho do set
faltam = total_album - len(figurinhas_unicas)

print(faltam)