import sys

def resolver():

    while True:
        try:
            linha_n = sys.stdin.readline()
            if not linha_n:
                break

            n = int(linha_n.strip())

            for _ in range(n):
                codigo = sys.stdin.readline().strip()
                grupos = codigo.split(' ')
                pontos_no_grupo = len(grupos[0])
                quantidade_grupos = len(grupos)
                deslocamento = pontos_no_grupo - 1 + 3 * (quantidade_grupos - 1)
                letra_decifrada = chr(97 + deslocamento)
                print(letra_decifrada)
        except EOFError:
            break

if __name__ == '__main__':
    resolver()