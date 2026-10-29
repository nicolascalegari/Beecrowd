import sys

def resolver_piramide():

  entrada = sys.stdin.read().split()
  if not entrada:
    return

  tamanho_n = int(entrada[0])
  indice = 1

  # Construção da matriz com os valores fornecidos
  matriz = []
  for linha_idx in range(tamanho_n):
    linha = []
    for coluna_idx in range(tamanho_n):
      linha.append(int(entrada[indice]))
      indice += 1
    matriz.append(linha)

  # Construção de uma matriz de soma prefixada por linha para acesso O(1)
  soma_prefixada = [[0] * (tamanho_n + 1) for _ in range(tamanho_n)]
  for linha_idx in range(tamanho_n):
    for coluna_idx in range(tamanho_n):
      soma_prefixada[linha_idx][coluna_idx + 1] = (
          soma_prefixada[linha_idx][coluna_idx] + matriz[linha_idx][coluna_idx]
      )

  def obter_soma_segmento(linha_idx, inicio, fim):
    return (
        soma_prefixada[linha_idx][fim + 1]
        - soma_prefixada[linha_idx][inicio]
    )

  # Tabela de Programação Dinâmica (DP)
  # tabela_dp[tamanho_piramide][inicio_coluna]
  # Calcular de cima para baixo (do topo N=1 até N)
  tabela_dp = [[0] * tamanho_n for _ in range(tamanho_n + 1)]

  # Preenchendo de cima para baixo
  for tamanho in range(1, tamanho_n + 1):
    # A linha na matriz correspondente à altura 'tamanho' da pirâmide (começando do topo = linha 0)
    linha_atual = tamanho - 1
    for inicio in range(tamanho_n - tamanho + 1):
      fim = inicio + tamanho - 1
      soma_atual = obter_soma_segmento(linha_atual, inicio, fim)

      if tamanho == 1:
        tabela_dp[tamanho][inicio] = soma_atual
      else:
        # Para formar a pirâmide de tamanho atual, ela precisa vir de uma
        # sub-pirâmide de tamanho-1 logo acima (podendo começar em 'inicio' ou 'inicio + 1')
        menor_acima = min(
            tabela_dp[tamanho - 1][inicio],
            tabela_dp[tamanho - 1][inicio + 1],
        )
        tabela_dp[tamanho][inicio] = soma_atual + menor_acima

  # O resultado final da pirâmide completa de tamanho N, começando no índice 0 da base/topo
  # Como a pirâmide completa tem tamanho N, o topo está na linha 0 e abrange o único segmento válido.
  print(tabela_dp[tamanho_n][0])


if __name__ == "__main__":
  resolver_piramide()