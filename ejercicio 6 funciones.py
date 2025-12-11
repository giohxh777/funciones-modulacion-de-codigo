# **************ZONA DE FUNCIONES***********
def solicitar_uso_cpu():
    """Solicita el porcentaje de uso de CPU."""
    return int(input("Ingrese uso de CPU (%) o valor negativo para salir: "))


def es_critico(uso):
    """Verifica si el uso supera el 90%."""
    return uso > 90


def registrar_alerta(contador):
    """Incrementa y muestra alerta crítica."""
    print(" Alerta: Uso Crítico de CPU")
    return contador + 1


def mostrar_reporte(mediciones, alertas):
    """Imprime el reporte final."""
    print("\n===== REPORTE FINAL DEL SERVIDOR =====")
    print(f"Mediciones registradas: {mediciones}")
    print(f"Alertas críticas: {alertas}")

#******codigo principal*********


total_mediciones = 0
alertas_criticas = 0

while True:
    uso = solicitar_uso_cpu()

    if uso < 0:
        break

    total_mediciones += 1

    if es_critico(uso):
        alertas_criticas = registrar_alerta(alertas_criticas)

mostrar_reporte(total_mediciones, alertas_criticas)
