seg_total = int(input())
hora = seg_total // 3600
resto = seg_total % 3600
minuto = resto // 60
segundo = resto % 60
print(f"{hora}:{minuto}:{segundo}")