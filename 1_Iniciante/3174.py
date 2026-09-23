def main():
    n = int(input())

    #Dicionario
    horas_por_grupo = {
        'bonecos': 0,
        'arquitetos': 0,
        'musicos': 0,
        'desenhistas': 0
    }

    contador = 0

    while contador < n:
        linha = input().split()
        grupo = linha[1]
        horas = int(linha[2])

        horas_por_grupo[grupo] += horas

        contador += 1

    total_brinquedos = 0
    total_brinquedos += horas_por_grupo['bonecos'] // 8
    total_brinquedos += horas_por_grupo['arquitetos'] // 4
    total_brinquedos += horas_por_grupo['musicos'] // 6
    total_brinquedos += horas_por_grupo['desenhistas'] // 12

    print(total_brinquedos)

if __name__ == "__main__":
    main()