# **************ZONA DE FUNCIONES***********

def solicitar_producto():
    """Pide precio unitario y cantidad."""
    precio = float(input("Ingrese precio unitario (0 para terminar): "))
    if precio == 0:
        return 0, 0
    cantidad = int(input("Ingrese la cantidad: "))
    return precio, cantidad


def calcular_subtotal(precio, cantidad):
    """Devuelve el subtotal del producto."""
    return precio * cantidad


def aplicar_descuento(subtotal):
    """Aplica el descuento según las reglas."""
    if subtotal > 1000:
        return subtotal * 0.10, "10% aplicado"
    elif subtotal > 500:
        return subtotal * 0.05, "5% aplicado"
    else:
        return 0, "No aplica descuento"


def mostrar_resumen(subtotal, descuento, mensaje):
    """Imprime los datos finales."""
    total_pagar = subtotal - descuento
    print("\n===== RESUMEN DE COMPRA =====")
    print(f"Subtotal sin descuento: ${subtotal:.2f}")
    print(f"Descuento: ${descuento:.2f} ({mensaje})")
    print(f"Total a pagar: ${total_pagar:.2f}")
#******codigo principal*********

subtotal_general = 0

while True:
    precio, cantidad = solicitar_producto()

    if precio == 0:
        break

    subtotal_general += calcular_subtotal(precio, cantidad)

descuento, mensaje = aplicar_descuento(subtotal_general)

mostrar_resumen(subtotal_general, descuento, mensaje)
