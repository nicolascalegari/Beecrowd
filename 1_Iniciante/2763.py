cpf = input()

cpfOrganizado = cpf.replace('-', '.')

cpfDividido = cpfOrganizado.split('.')

for parte in cpfDividido:
    print(parte)