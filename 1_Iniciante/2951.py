import sys

def main():

    primeira_linha = sys.stdin.readline().split()
    if not primeira_linha:
        return
    n = int(primeira_linha[0])
    g = int(primeira_linha[1])
    
    runas_valores = {}
    
    for _ in range(n):
        linha = sys.stdin.readline().split()
        nome_runa = linha[0]
        valor_runa = int(linha[1])
        runas_valores[nome_runa] = valor_runa
        
    x = int(sys.stdin.readline().strip())
    
    runas_recitadas = sys.stdin.readline().split()
    
    amizade_total = 0
    for runa in runas_recitadas:
        if runa in runas_valores:
            amizade_total += runas_valores[runa]
            
    print(amizade_total)
    
    if amizade_total >= g:
        print("You shall pass!")
    else:
        print("My precioooous")

if __name__ == '__main__':
    main()
