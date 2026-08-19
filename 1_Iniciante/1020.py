dias_total = int(input())
ano = dias_total // 365
resto = dias_total % 365
mes = resto // 30
dia = dias_total - (ano * 365 + mes * 30)
print(f"{ano} ano(s)\n{mes} mes(es)\n{dia} dia(s)") 
