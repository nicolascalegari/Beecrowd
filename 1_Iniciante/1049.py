import sys

def resolver():
    # Estrutura de árvore usando dicionários aninhados
    arvore_animais = {
        'vertebrado': {
            'ave': {
                'carnivoro': 'aguia',
                'onivoro': 'pomba'
            },
            'mamifero': {
                'onivoro': 'homem',
                'herbivoro': 'vaca'
            }
        },
        'invertebrado': {
            'inseto': {
                'hematofago': 'pulga',
                'herbivoro': 'lagarta'
            },
            'anelideo': {
                'hematofago': 'sanguessuga',
                'onivoro': 'minhoca'
            }
        }
    }
    
    # Lê as 3 linhas de entrada fornecidas pelo Beecrowd
    linhas = sys.stdin.read().splitlines()
    if len(linhas) < 3:
        return
        
    p1 = linhas[0].strip()
    p2 = linhas[1].strip()
    p3 = linhas[2].strip()
    
    # Navega pelo dicionário usando as palavras como chaves
    resultado = arvore_animais[p1][p2][p3]
    
    # Imprime o animal encontrado acompanhado da quebra de linha
    print(resultado)

if __name__ == '__main__':
    resolver()
