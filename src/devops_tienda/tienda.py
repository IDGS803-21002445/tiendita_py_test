def calcular_precio(precio, descuento):
    if precio < 0:
        raise ValueError("Precio invalido")
    if not 0 <= descuento <= 100:
        raise ValueError("Descuento invalido")
    return precio * (1 - descuento / 100)
 
 
def calcular_iva(precio):
    return precio * 1.16