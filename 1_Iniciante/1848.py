import sys

def main():
    linhas = sys.stdin.read().splitlines()

    soma_atual = 0
    gritos = 0

    for linha in linhas:
        if linha == 'caw caw':
            print(soma_atual)
            soma_atual = 0
            gritos += 1
            if gritos == 3:
                break

        else:
            binario = linha.replace('-', '0').replace('*', '1')
            valor = int(binario, 2)
            soma_atual += valor

if __name__ == '__main__':
    main()