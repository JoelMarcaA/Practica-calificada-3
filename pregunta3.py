import math

class CIRCULO:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        # El área de un círculo se calcula mediante la fórmula: A = π * r^2
        area = math.pi * (self.radio ** 2)
        return area

# Ejemplo de uso
def main():
    try:
        # Solicitar al usuario el radio del círculo
        radio = float(input("Introduce el radio del círculo: "))

        # Crear una instancia de la clase CIRCULO
        mi_circulo = CIRCULO(radio)

        # Calcular y mostrar el área del círculo
        area = mi_circulo.calcular_area()
        print(f"El área del círculo con radio {radio} es: {area:.2f}")

    except ValueError:
        print("Error: Asegúrate de introducir un número válido para el radio.")

if __name__ == "__main__":
    main()
