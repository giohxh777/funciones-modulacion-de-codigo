# **************ZONA DE FUNCIONES***********

def solicitar_unidades():
    """Pide cuántas unidades fueron producidas."""
    return int(input("Ingrese cantidad de unidades producidas en el lote (0 para terminar): "))


def evaluar_unidad(numero):
    """Evalúa si una unidad está defectuosa o no."""
    estado = input(f"Unidad {numero}: ¿Es defectuosa? (S/N): ").upper()
    return estado == "S"


def mostrar_resultados(total, defectuosas):
    """Muestra el resumen de producción."""
    print("\n===== REPORTE DE PRODUCCIÓN =====")
    print(f"Total de unidades producidas: {total}")
    print(f"Unidades defectuosas: {defectuosas}")
    print(f"Unidades buenas: {total - defectuosas}")

#******codigo principal*********

total_unidades = solicitar_unidades()

if total_unidades == 0:
    print("No se ingresaron unidades. Proceso finalizado.")
else:
    defectuosas = 0

    for i in range(1, total_unidades + 1):
        if evaluar_unidad(i):
            defectuosas += 1

    mostrar_resultados(total_unidades, defectuosas)
