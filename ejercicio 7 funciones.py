# **************ZONA DE FUNCIONES***********

def solicitar_monto():
    """Solicita el monto de ventas del vendedor."""
    return float(input("Ingrese monto de ventas del vendedor (0 para terminar): "))


def cumple_meta(monto, meta):
    """Verifica si el vendedor cumplió o no la meta."""
    return monto >= meta


def registrar_cumplimiento(contador):
    """Incrementa contador de vendedores que cumplieron la meta."""
    print("✔ Meta cumplida. ¡Felicidades al vendedor!")
    return contador + 1


def registrar_no_cumplimiento():
    """Mensaje cuando el vendedor no cumple la meta."""
    print("X Meta NO cumplida.")


def mostrar_reporte(total_vendedores, cumplidores):
    """Muestra el resumen final."""
    print("\n===== REPORTE FINAL DE METAS =====")
    print(f"Total de vendedores procesados: {total_vendedores}")
    print(f"Vendedores con meta cumplida: {cumplidores}")
    
#******codigo principal*********

META = 5000
total_vendedores = 0
cumplieron = 0

while True:
    monto = solicitar_monto()

    if monto == 0:
        break

    total_vendedores += 1

    if cumple_meta(monto, META):
        cumplieron = registrar_cumplimiento(cumplieron)
    else:
        registrar_no_cumplimiento()

mostrar_reporte(total_vendedores, cumplieron)

