import sys

def main():
    tabela_vitamina = {
        "suco de laranja": 120,
        "morango fresco": 85,
        "mamao": 85,
        "goiaba vermelha": 70,
        "manga": 56,
        "laranja": 50,
        "brocolis": 34
    }
    
    linhas = sys.stdin.read().splitlines()
    if not linhas:
        return
        
    ponteiro = 0
    while ponteiro < len(linhas):
        T = int(linhas[ponteiro])
        ponteiro += 1
        
        if T == 0:
            break
            
        total_vitamina = 0

        for _ in range(T):
            linha_alimento = linhas[ponteiro].strip()
            ponteiro += 1
            
            partes = linha_alimento.split(' ', 1)
            quantidade = int(partes[0])
            alimento = partes[1]
            
            total_vitamina += quantidade * tabela_vitamina[alimento]
            
        if total_vitamina > 130:
            print(f"Menos {total_vitamina - 130} mg")
        elif total_vitamina < 110:
            print(f"Mais {110 - total_vitamina} mg")
        else:
            print(f"{total_vitamina} mg")

if __name__ == '__main__':
    main()
