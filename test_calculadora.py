import pytest
from main import Calculadora

@pytest.fixture
def calcular():
    return Calculadora()

def teste_soma(calcular):
    assert calcular.soma(1,2) == 3
    assert calcular.soma(0,0) == 0
    assert calcular.soma(-1,1) == 0

def teste_sub(calcular):
    assert calcular.sub(3,2) == 1
    assert calcular.sub(0,0) == 0
    assert calcular.sub(10,5) == 5

def teste_mult(calcular):
    assert calcular.mult(1,2) == 2
    assert calcular.mult(3,5) == 15
    assert calcular.mult(2,2) == 4

def teste_div(calcular):
    assert calcular.div(10,5) == 2
    assert calcular.div(20,4) == 5
    assert calcular.div(15,5) == 3

    with pytest.raises(ValueError):
        calcular.div(5, 0)