regras = {
    "tesoura": ["papel", "lagarto"],
    "papel": ["pedra", "spock"],
    "pedra": ["lagarto", "tesoura"],
    "lagarto": ["spock", "papel"],
    "spock": ["tesoura", "pedra"]
}

t = int(input())

for i in range(1, t + 1):
    sheldon, raj = input().strip().lower().split()
    
    if sheldon == raj:
        resultado = "De novo!"
    elif raj in regras[sheldon]:
        resultado = "Bazinga!"
    else:
        resultado = "Raj trapaceou!"
        
    print(f"Caso #{i}: {resultado}")