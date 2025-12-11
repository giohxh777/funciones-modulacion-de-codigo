# **************ZONA DE FUNCIONES***********

def solicitar_numero_pedidos():
    """Pide la cantidad total de pedidos a procesar."""
    return int(input("Ingrese la cantidad de pedidos a procesar: "))


def solicitar_calificacion(numero_pedido):
    """Solicita la calificación para un pedido."""
    return int(input(f"Calificación del pedido #{numero_pedido} (1 a 5, 0 para terminar): "))


def validar_calificacion(calificacion):
    """Verifica si la calificación está en el rango permitido."""
    return 1 <= calificacion <= 5


def acumular_puntos(total, calificacion):
    """Suma los puntos al total."""
    return total + calificacion


def contar_excelentes(contador, calificacion):
    """Incrementa contador si la calificación es 5."""
    if calificacion == 5:
        return contador + 1
    return contador


def mostrar_reporte(total_pedidos, puntos_totales, excelentes):
    """Imprime el reporte final."""
    promedio = puntos_totales / total_pedidos if total_pedidos > 0 else 0

    print(f"Pedidos procesados: {total_pedidos}")
    print(f"Promedio general: {promedio:.2f}")
    print(f"Pedidos excelentes: {excelentes}")
#******codigo principal*********

cantidad_pedidos = solicitar_numero_pedidos()
 
procesados = 0
total_puntos = 0
excelentes = 0

for i in range(1, cantidad_pedidos + 1):
    calificacion = solicitar_calificacion(i)

    if calificacion == 0:
        print("Proceso terminado antes de completar todos los pedidos.")
        break

    if not validar_calificacion(calificacion):
        print("X Calificación inválida. Debe estar entre 1 y 5.")
        continue

    procesados += 1
    total_puntos = acumular_puntos(total_puntos, calificacion)
    excelentes = contar_excelentes(excelentes, calificacion)

mostrar_reporte(procesados, total_puntos, excelentes)


    
    
        
  
      
 