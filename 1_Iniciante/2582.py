musicas = [
    "PROXYCITY", "P.Y.N.G.", "DNSUEY!", "SERVERS",
    "HOST!", "CRIPTONIZE", "OFFLINE DAY", "SALT",
    "ANSWER!", "RAR?", "WIFI ANTENNAS"
]

c = int(input())

for _ in range(c):

    x, y = map(int,input().split())

    soma = x + y

    print(musicas[soma])