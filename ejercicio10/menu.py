# 

from geometria import Circulo, Rectangulo, Cuadrado

def mostrar_menu():
    print("Menú:")
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un rectángulo")
    print("3. Calcular el área de un cuadrado")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            radio = float(input("Ingrese el radio del círculo: "))
            circulo = Circulo(radio)
            print(f"El área del círculo es: {circulo.calcular_area()}")
        elif opcion == "2":
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            rectangulo = Rectangulo(base, altura)
            print(f"El área del rectángulo es: {rectangulo.calcular_area()}")
        elif opcion == "3":
            lado = float(input("Ingrese el lado del cuadrado: "))
            cuadrado = Cuadrado(lado)
            print(f"El área del cuadrado es: {cuadrado.calcular_area()}")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
