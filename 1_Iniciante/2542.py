while True:
    try:
        linha_n = input()
        if not linha_n:
            break
        n = int(linha_n)
        
        m, l = map(int, input().split())
        
        baralho_marcos = []
        for _ in range(m):
            carta = list(map(int, input().split()))
            baralho_marcos.append(carta)
            
        baralho_leonardo = []
        for _ in range(l):
            carta = list(map(int, input().split()))
            baralho_leonardo.append(carta)
            
        cm, cl = map(int, input().split())
        cm -= 1
        cl -= 1
        
        atributo = int(input()) - 1
        
        valor_marcos = baralho_marcos[cm][atributo]
        valor_leonardo = baralho_leonardo[cl][atributo]
        
        if valor_marcos > valor_leonardo:
            print("Marcos")
        elif valor_leonardo > valor_marcos:
            print("Leonardo")
        else:
            print("Empate")
            
    except EOFError:
        break
