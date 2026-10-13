n = int(input())

total_casas = n * n

casas_brancas = (total_casas + 1) // 2
casas_pretas = total_casas // 2

print(f"{casas_brancas} casas brancas e {casas_pretas} casas pretas")