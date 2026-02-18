def juros_compostos(valor, taxa, meses):
    taxa = taxa / 100
    montante = valor * (1 + taxa) ** meses
    return round(montante, 2)

def simulacao_investimento(aporte, taxa, meses):
    taxa = taxa / 100
    total = 0
    for i in range(meses):
        total = (total + aporte) * (1 + taxa)
    return round(total, 2)
