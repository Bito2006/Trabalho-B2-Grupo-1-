from funcoes import *

def test_calcular_internet():
    result = calculo_gasto_internet(60)
    assert result == 20


def test_calcular_local():
    result = calculo_ligacao_local(150)
    assert result == 52.5

def test_calcular_interurbana():
    result = calculo_ligacao_interurbana(150)
    assert result == 90


def test_calcular_torpedos():
    result = calculo_torpedos(80)
    assert result == 16

def test_calcular_fatura():
    result = calcular_fatura(100, 100, 100, 10)
    assert result == 147, 'Internet'

