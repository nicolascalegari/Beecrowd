def validar_e_verificar_rodizio():

    n = int(input())
    
    for _ in range(n):
        placa = input().strip()
        
        if (len(placa) == 8 and 
                placa[0:3].isalpha() and 
                placa[0:3].isupper() and 
                placa[3] == '-' and 
                placa[4:8].isdigit()):
            
            ultimo_digito = placa[-1]
            
            if ultimo_digito in '12':
                print("MONDAY")
            elif ultimo_digito in '34':
                print("TUESDAY")
            elif ultimo_digito in '56':
                print("WEDNESDAY")
            elif ultimo_digito in '78':
                print("THURSDAY")
            elif ultimo_digito in '90':
                print("FRIDAY")
        else:
            print("FAILURE")

validar_e_verificar_rodizio()