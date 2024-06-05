from funcoes import * 

internet = float(input('Informe o gasto de internet: '))
ligacao_local = float(input('Informe o gasto de minutos em ligação local: '))
ligacao_interurbana = float(input('Informe o gasto de minutos em ligação interurbana: '))
torpedos = float(input('Informe o gasto de torpedos: '))

# gasto_internet = calculo_gasto_internet(internet)
# gasto_ligacao_local = calculo_ligacao_local(ligacao_local)
# gasto_ligacao_interurbana = calculo_ligacao_interurbana(ligacao_interurbana)
# gasto_torpedo = calculo_torpedos(torpedos)

valor_sem_desconto, tipo_desconto, valor_desconto, valor_com_desconto  = calcular_fatura(internet, ligacao_local, ligacao_interurbana, torpedos)

print(f' O valor total sem desconto é de R${valor_sem_desconto:.2f} \n O tipo de desconto concedido é: {tipo_desconto} \n O valor total de descontos foi de R${valor_desconto:.2f} \n O valor total do com descontos é de: R${valor_com_desconto}')


