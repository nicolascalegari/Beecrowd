import sys

def resolver():
    linhas = sys.stdin.read().splitlines()
    
    for coluna in linhas:
        coluna = coluna.strip()
        if not coluna:
            continue
        
        if len(coluna) > 3 or (len(coluna) == 3 and coluna > "XFD"):
            print("Essa coluna nao existe Tobias!")
            continue

        numero = 0
        for letra in coluna:
            numero = numero * 26 + (ord(letra) - 64)
            
        print(numero)

if __name__ == "__main__":
    resolver()
