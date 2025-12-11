# **************ZONA DE FUNCIONES***********



def solicitar_codigo():
    """Pide al usuario un código de identificación."""
    return input("Ingrese código del empleado (o SALIR para terminar): ").upper()


def validar_codigo(codigo_ingresado, codigo_correcto):
    """Verifica si el código es el correcto."""
    return codigo_ingresado == codigo_correcto


def registrar_acceso_exitoso(contador):
    """Incrementa el contador de accesos permitidos."""
    print("✔ Acceso permitido. Registro exitoso.")
    return contador + 1


def registrar_acceso_denegado(contador):
    """Incrementa el contador de accesos denegados."""
    print("x Acceso denegado. Código incorrecto.")
    return contador + 1


def mostrar_resumen(permitidos, denegados):
    """Muestra el resumen final del sistema."""
    print("\n===== RESUMEN DEL SISTEMA =====")
    print(f"Accesos Permitidos : {permitidos}")
    print(f"Accesos Denegados  : {denegados}")
    print("Proceso finalizado.")


#******codigo principal*********

codigo_especial = "SENA321"
accesos_permitidos = 0
accesos_denegados = 0

while True:
    codigo = solicitar_codigo()

    if codigo == "SALIR":
        break

    if validar_codigo(codigo, codigo_especial):
        accesos_permitidos = registrar_acceso_exitoso(accesos_permitidos)
    else:
        accesos_denegados = registrar_acceso_denegado(accesos_denegados)

mostrar_resumen(accesos_permitidos, accesos_denegados)
