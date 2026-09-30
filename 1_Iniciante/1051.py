salario = float(input())

if salario <= 2000.00:
    print("Isento")
else:
    faixas = [
        (1000.00, 0.08),
        (1500.00, 0.18),
        (float('inf'), 0.28)
    ]

    imposto = 0.0
    valor_tributavel = salario - 2000.00 # Parte isenta

    for tamanho_faixa, aliquota in faixas:
        if valor_tributavel > tamanho_faixa:
            imposto += tamanho_faixa * aliquota
            valor_tributavel -= tamanho_faixa
        else:
            imposto += valor_tributavel * aliquota
            break

    print(f"R$ {imposto:.2f}")