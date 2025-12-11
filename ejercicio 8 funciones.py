# **************ZONA DE FUNCIONES***********

def solicitar_edad():
    """Pide la edad del participante."""
    return int(input("Ingrese la edad del participante (0 para terminar): "))


def pertenece_rango(edad):
    """Indica si la edad está dentro del rango objetivo 25-45."""
    return 25 <= edad <= 45


def registrar_objetivo(contador):
    """Incrementa el contador de personas en el rango objetivo."""
    print("✔ Público objetivo registrado.")
    return contador + 1


def mostrar_reporte(total_personas, total_edades, objetivo):
    """Muestra el informe completo de la encuesta."""
    promedio = total_edades / total_personas if total_personas > 0 else 0

    print("\n===== REPORTE DE ENCUESTA =====")
    print(f"Total participantes: {total_personas}")
    print(f"Promedio de edad: {promedio:.2f}")
    print(f"Público objetivo (25-45 años): {objetivo}")
