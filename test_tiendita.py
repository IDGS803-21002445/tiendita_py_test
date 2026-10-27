
import pytest
from tienda import calcular_precio
from tienda import calcular_iva


def test_precio_con_descuento():
    precio = 200
    descuento = 25
    resultado_esperado = 150

    assert calcular_precio(precio, descuento) == resultado_esperado


def test_precio_con_iva():
    precio = 100
    resultado_esperado = 116

    assert calcular_iva(precio) == pytest.approx(resultado_esperado)


def test_precio_sin_descuento():
    precio = 500
    descuento = 0
    resultado_esperado = 500

    assert calcular_precio(precio, descuento) == resultado_esperado


def test_descuento_invalido():
    precio = 100
    descuento = 200

    with pytest.raises(ValueError):
        calcular_precio(precio, descuento)
