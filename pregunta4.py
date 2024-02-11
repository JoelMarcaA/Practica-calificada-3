class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        # El área de un rectángulo se calcula mediante la fórmula: A = largo * ancho
        area = self.largo * self.ancho
        return area

# Ejemplo de uso
def main():
    try:
        # Solicitar al usuario el largo y ancho del rectángulo
        largo = float(input("Introduce el largo del rectángulo: "))
        ancho = float(input("Introduce el ancho del rectángulo: "))

        # Crear una instancia de la clase RECTANGULO
        mi_rectangulo = RECTANGULO(largo, ancho)

        # Calcular y mostrar el área del rectángulo
        area = mi_rectangulo.calcular_area()
        print(f"El área del rectángulo con largo {largo} y ancho {ancho} es: {area:.2f}")

    except ValueError:
        print("Error: Asegúrate de introducir números válidos para el largo y ancho del rectángulo.")

if __name__ == "__main__":
    main()
