def calculo_gasto_internet(mbs: float):
    total_gasto = mbs * 0.50
    return total_gasto


def calculo_ligacao_local(min: float):
    total_gasto = min * 0.35
    return total_gasto


def calculo_ligacao_interurbana(min: float):
    total_gasto = min * 0.60
    return total_gasto


def calculo_torpedos(torpedos: int):
    total_gasto = torpedos * 0.20
    return total_gasto


def calcular_fatura(internet, ligacao_local, ligacao_interurbana, torpedos):
    # Calcula o custo de cada serviço
    custo_internet = calculo_gasto_internet(internet)
    custo_ligacao_local = calculo_ligacao_local(ligacao_local)
    custo_ligacao_interurbana = calculo_ligacao_interurbana(ligacao_interurbana)
    custo_torpedo = calculo_torpedos(torpedos)

    # Calcula o total da fatura sem desconto
    total_sem_desconto = custo_internet + custo_ligacao_local + custo_ligacao_interurbana + custo_torpedo

    # Aplica os descontos
    maior_desconto = 0
    tipo_desconto = "Nenhum"

    if internet > 50:
        desconto = custo_internet * 0.05
        if desconto > maior_desconto:
            maior_desconto = desconto
            tipo_desconto = "Internet"

    if ligacao_local > 200:
        desconto = custo_ligacao_local * 0.10
        if desconto > maior_desconto:
            maior_desconto = desconto
            tipo_desconto = "Ligações locais"

    if ligacao_interurbana > 150:
        desconto = custo_ligacao_interurbana * 0.10
        if desconto > maior_desconto:
            maior_desconto = desconto
            tipo_desconto = "Ligações interurbanas"

    if torpedos > 50:
        desconto = custo_torpedo * 0.20
        if desconto > maior_desconto:
            maior_desconto = desconto
            tipo_desconto = "Torpedos"

    # Calcula o total da fatura com desconto
    total_com_desconto = total_sem_desconto - maior_desconto

    return total_sem_desconto, tipo_desconto, maior_desconto, total_com_desconto

