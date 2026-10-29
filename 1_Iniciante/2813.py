import sys

def resolver_evitando_chuva():

  tokens = sys.stdin.read().split()
  if not tokens:
    return

  indice = 0

  while indice < len(tokens):
    total_dias = int(tokens[indice])
    indice += 1

    comprados_casa = 0
    comprados_escritorio = 0
    guarda_chuvas_casa = 0
    guarda_chuvas_escritorio = 0

    for _ in range(total_dias):
      ida_previsao = tokens[indice]
      volta_previsao = tokens[indice + 1]
      indice += 2

      # Verificação para a ida ao trabalho
      if ida_previsao == "chuva":
        if guarda_chuvas_casa > 0:
          guarda_chuvas_casa -= 1
        else:
          comprados_casa += 1
        # O guarda-chuva é levado e fica disponível no escritório
        guarda_chuvas_escritorio += 1

      # Verificação para a volta para casa
      if volta_previsao == "chuva":
        if guarda_chuvas_escritorio > 0:
          guarda_chuvas_escritorio -= 1
        else:
          comprados_escritorio += 1
        # O guarda-chuva é levado e fica disponível em casa
        guarda_chuvas_casa += 1

    # Imprime o resultado para o caso de teste atual
    print(f"{comprados_casa} {comprados_escritorio}")

if __name__ == "__main__":
  resolver_evitando_chuva()