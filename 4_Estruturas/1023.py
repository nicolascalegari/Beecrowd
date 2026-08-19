import sys
import math

def resolver():
    # Lê toda a entrada de uma vez só (funciona so no beecrowd)
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    num_cidade = 1
    primeira_cidade = True

    while True:
        try:
            n_str = next(iterator)
        except StopIteration:
            break
        
        n = int(n_str)
        if n == 0:
            break

        # Linha em branco entre as cidades (menos na primeira)
        if not primeira_cidade:
            print()
        primeira_cidade = False

        total_pessoas = 0
        total_consumo = 0
        
        # Vetor de contagem indexado pelo consumo médio por pessoa (0 a 200 m³)
        # Evita a necessidade de ordenar listas dinâmicas a cada iteração
        consumo_contagem = [0] * 201

        for _ in range(n):
            X = int(next(iterator))  # quantidade de moradores
            Y = int(next(iterator))  # consumo total do imóvel
            
            total_pessoas += X
            total_consumo += Y
            
            # Divisão inteira trunca o consumo por pessoa exigido no problema
            consumo_medio = Y // X
            consumo_contagem[consumo_medio] += X

        # Monta a string de saída para os consumos ordenados
        saida_moradores = []
        for c in range(201):
            if consumo_contagem[c] > 0:
                saida_moradores.append(f"{consumo_contagem[c]}-{c}")

        print(f"Cidade# {num_cidade}:")
        print(" ".join(saida_moradores))
        
        # Truncamento manual em 2 casas decimais sem arredondamento flutuante
        # Multiplicar por 100, truncar com math.floor e depois dividir evita erros do round()
        media_total = math.floor((total_consumo / total_pessoas) * 100) / 100
        print(f"Consumo medio: {media_total:.2f} m3.")

        num_cidade += 1

if __name__ == "__main__": # Chamar a função quando der play
    resolver()
