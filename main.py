from tienda import calcular_precio, calcular_iva

def main():
    try:
        precio = float(input("Ingresa el precio del producto: $"))
        descuento = float(input("Ingresa el porcentaje de descuento: "))

        precio_final = calcular_precio(precio, descuento)
        total = calcular_iva(precio_final)

        print(f"Precio con descuento: ${precio_final:.2f}")
        print(f"Total con IVA: ${total:.2f}")

    except (ValueError, TypeError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()