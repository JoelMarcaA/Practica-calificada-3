def obtener_calificaciones():
    while True:
        try:
            # Solicitar al usuario la entrada de calificaciones
            entrada_usuario = input("Ingrese las calificaciones separadas por comas: ")
            
            # Dividir la cadena en calificaciones individuales
            calificaciones_str = entrada_usuario.split(',')
            
            # Convertir cada calificación a un entero
            calificaciones_entero = [int(calificacion) for calificacion in calificaciones_str]
            
            return calificaciones_entero
        except ValueError:
            print("Error: Tipo de dato no válido. Introduzca solo números separados por comas.")

