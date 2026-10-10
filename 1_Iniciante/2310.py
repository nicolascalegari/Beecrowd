n = int(input())

tentativas_totais = [0,0,0]
sucessos_totais = [0,0,0]

for _ in range(n):
    nome = input()
    
    s, b, a = map(int, input().split())
    tentativas_totais[0] += s
    tentativas_totais[1] += b
    tentativas_totais[2] += a
    
    s1, b1, a1 = map(int,input().split())
    sucessos_totais[0] += s1
    sucessos_totais[1] += b1
    sucessos_totais[2] += a1
    
porc_saque = (sucessos_totais[0] / tentativas_totais[0]) * 100
porc_bloqueio = (sucessos_totais[1] / tentativas_totais[1]) * 100
porc_ataque = (sucessos_totais[2] / tentativas_totais[2]) * 100

print(f"Pontos de Saque: {porc_saque:.2f} %.")
print(f"Pontos de Bloqueio: {porc_bloqueio:.2f} %.")
print(f"Pontos de Ataque: {porc_ataque:.2f} %.")
                  