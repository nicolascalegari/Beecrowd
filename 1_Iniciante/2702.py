ca, ba, pa = map(int, input().split())
cr, br, pr = map(int, input().split())

nao_atend = 0

if cr > ca:
    nao_atend += cr - ca

if br > ba:
    nao_atend += br - ba

if pr > pa:
    nao_atend += pr - pa

print(nao_atend)