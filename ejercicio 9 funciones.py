# **************ZONA DE FUNCIONES***********

def solicitar_venta():
    """Pide la cantidad vendida en el día."""
    return int(input("Ingrese cantidad vendida hoy (0 para terminar): "))


def actualizar_stock(stock, ventas):
    """Resta las ventas al stock."""
    return stock - ventas


def requiere_reposicion(stock, punto_reposicion):
    """Verifica si el stock está por debajo o igual al punto crítico."""
    return stock <= punto_reposicion


def mostrar_aviso():
    """Mensaje de urgencia por reposición."""
    print(" AVISO: Reposición Urgente Necesaria")


def mostrar_reporte(stock):
    """Muestra el estado final del inventario."""
    print("===== REPORTE FINAL DE INVENTARIO =====")
    print(f"Stock final: {stock} unidades")

#******codigo principal*********


stock = 50
punto_reposicion = 10

while True:
    ventas = solicitar_venta()

    if ventas == 0:
        break

    stock = actualizar_stock(stock, ventas)

    if requiere_reposicion(stock, punto_reposicion):
        mostrar_aviso()
        break

mostrar_reporte(stock)
