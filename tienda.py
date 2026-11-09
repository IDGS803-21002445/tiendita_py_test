def calcular_precio(precio, descuento):
    validar_descuento(descuento)
    total = precio - (precio * descuento / 100)
    return total


def calcular_iva(total):
    return total * 1.16


def validar_descuento(descuento):
    if descuento < 0 or descuento > 100:
        raise ValueError("El descuento debe estar entre 0 y 100")


def calcular_envio(subtotal):
    if subtotal < 0:
        raise ValueError("Subtotal invalido")
    if subtotal > 500:
        return 0
    return 80
