def resolver():

    data = input().strip()

    dia = data[0:2]
    mes = data[3:5]
    ano = data[6:8]

    print(f"{mes}/{dia}/{ano}")
    print(f"{ano}/{mes}/{dia}")
    print(f"{dia}-{mes}-{ano}")

resolver()