
# **************ZONA DE FUNCIONES***********


def solicitar_transaccion():
    """Solicita el tipo de transacción (D/R) o FIN."""
    tipo = input("Ingrese tipo de transacción (D=Depósito, R=Retiro, FIN para terminar): ").upper()
    return tipo


def solicitar_monto():
    """Solicita el monto de la transacción."""
    return float(input("Ingrese el monto: "))


def procesar_deposito(saldo, monto):
    """Suma el monto al saldo."""
    return saldo + monto


def procesar_retiro(saldo, monto):
    """Resta el monto si no deja saldo negativo."""
    if saldo - monto < 0:
        print(" X Error: El retiro generaría saldo negativo. Operación no realizada.")
        return saldo, False
    else:
        return saldo - monto, True


def mostrar_resumen(transacciones_validas, saldo_final):
    """Muestra el estado final del sistema bancario."""
    print("\n===== RESUMEN DIARIO =====")
    print(f"Transacciones válidas: {transacciones_validas}")
    print(f"Saldo final: ${saldo_final:.2f}")

#******codigo principal*********

saldo = 1000
transacciones_validas = 0

while True:
    tipo = solicitar_transaccion()

    if tipo == "FIN":
        break

    if tipo not in ("D", "R"):
        print(" X Tipo inválido. Intente nuevamente.")
        continue

    monto = solicitar_monto()

    if tipo == "D":
        saldo = procesar_deposito(saldo, monto)
        transacciones_validas += 1

    elif tipo == "R":
        saldo, ok = procesar_retiro(saldo, monto)
        if ok:
            transacciones_validas += 1

mostrar_resumen(transacciones_validas, saldo)
