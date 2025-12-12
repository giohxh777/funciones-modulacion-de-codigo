# **************ZONA DE FUNCIONES***********

def solicitar_horas():
    """Solicita las horas extras trabajadas."""
    return int(input("Ingrese horas extra trabajadas por el empleado (0 para terminar): "))


def calcular_bonificacion(horas):
    """
    Calcula la bonificación:
    - $15 por hora si las horas > 5
    - $10 por hora si las horas <= 5
    """
    if horas > 5:
        return horas * 15
    else:
        return horas * 10


def mostrar_calculo(horas, bonificacion):
    """Imprime los valores por empleado."""
    print(f"Horas extra: {horas} -> Bonificación: ${bonificacion}")


def mostrar_reporte(total_empleados, total_bonificaciones):
    """Resumen final."""
    print("\n===== REPORTE DE BONIFICACIONES =====")
    print(f"Empleados procesados: {total_empleados}")
    print(f"Total pagado en bonificaciones: ${total_bonificaciones}")

#******codigo principal*********

total_empleados = 0
total_bonificaciones = 0

while True:
    horas = solicitar_horas()

    if horas == 0:
        break

    total_empleados += 1
    bonificacion = calcular_bonificacion(horas)
    total_bonificaciones += bonificacion

    mostrar_calculo(horas, bonificacion)

mostrar_reporte(total_empleados, total_bonificaciones)
