import sys

def main():
    # Lê a primeira linha com a quantidade de casos
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
        
    n_casos = int(input_data[0])
    
    # Processa estritamente a quantidade N de linhas informadas
    for i in range(1, n_casos + 1):
        texto = input_data[i]
        
        # Deslocar letras puras (A-Z e a-z) 3 posições para a direita
        passo1 = ""
        for char in texto:
            if char.isalpha():
                passo1 += chr(ord(char) + 3)
            else:
                passo1 += char
                
        # Inverter a string obtida
        passo2 = passo1[::-1]
        
        # Deslocar caracteres da metade em diante 1 posição para a esquerda
        # O truncamento da metade em Python precisa ser exato para strings ímpares/pares
        metade = len(passo2) // 2
        
        parte_inicial = passo2[:metade]
        parte_final = ""
        
        for char in passo2[metade:]:
            parte_final += chr(ord(char) - 1)
            
        # Junta as duas partes modificadas
        resultado_final = parte_inicial + parte_final
        
        # Exibe o resultado na tela
        print(resultado_final)

if __name__ == "__main__":
    main()
