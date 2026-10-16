import re
import sys

def resolver():
    entrada = sys.stdin.read()
    if not entrada.strip():
        return

    # O padrão '\d+' encontra todas as sequências de números na entrada
    numeros = list(map(int, re.findall(r'\d+', entrada)))
    
    # Desempacota os números diretamente nas variáveis de início e fim
    d1, h1, m1, s1, d2, h2, m2, s2 = numeros

    # Converte os dois momentos diretamente para segundos
    inicio_segundos = d1 * 86400 + h1 * 3600 + m1 * 60 + s1
    fim_segundos = d2 * 86400 + h2 * 3600 + m2 * 60 + s2

    # Calcula a diferença total de tempo em segundos
    total = fim_segundos - inicio_segundos

    # Extrai os dias, horas, minutos e segundos usando divisão inteira (//) e resto (%)
    dias = total // 86400
    horas = (total % 86400) // 3600
    minutos = (total % 3600) // 60
    segundos = total % 60

    print(f"{dias} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)")

if __name__ == '__main__':
    resolver()
