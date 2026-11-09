import pytest
from tienda import calcular_precio, calcular_iva

def test_integracion_precio_descuento_iva():
    precio = 200
    descuento = 25

    precio_final = calcular_precio(precio, descuento)
    total = calcular_iva(precio_final)

    assert precio_final == 150
    assert total == pytest.approx(174)

def test_integracion_descuento_invalido():
    precio = 200
    descuento = 150

    with pytest.raises(ValueError):
        precio_final = calcular_precio(precio, descuento)
        calcular_iva(precio_final)

def test_integracion_descuento_total():
    precio = 200
    descuento = 100

    precio_final = calcular_precio(precio, descuento)
    total = calcular_iva(precio_final)

    assert precio_final == 0
    assert total == 0