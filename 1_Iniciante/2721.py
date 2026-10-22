renas = ["Dasher", "Dancer", "Prancer", "Vixen", "Comet", "Cupid", "Donner", "Blitzen", "Rudolph"]

bolas_de_neve = list(map(int,input().split()))

total_bolas = sum(bolas_de_neve)

idx_rena = (total_bolas - 1) % 9

print(renas[idx_rena])