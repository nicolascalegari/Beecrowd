codigo, qtd = map(int, input().split())
preco = 0
if codigo == 1:
   preco = 4.00
elif codigo == 2:
   preco = 4.50
elif codigo == 3:
   preco = 5.00
elif codigo == 4:
   preco = 2.00
elif codigo == 5:
   preco = 1.50 

print(f"Total: R$ {qtd * preco:.2f}")