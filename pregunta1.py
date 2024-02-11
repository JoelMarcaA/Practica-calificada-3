#programa que solicite al usuario la fraccion para el calculo del combustible.

def calcular_porcentaje(fraction):
    try:
        x, y = map(int, fraction.split('/'))
        if x <= 0 or y == 0:
            raise ValueError("X debe ser mayor que 0 y Y no puede ser 0")
        if x > y:
            raise ValueError("X debe ser menor o igual a Y")
        valor_evaluado = (x / y) * 100
        if valor_evaluado < 1:
            return 'E'
        elif valor_evaluado > 99:
            return 'F'
        else:
            return f'{round(valor_evaluado)}%'
    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero (Y no puede ser 0)")
        return None

def main():
    while True:
        fraction = input("Ingrese una fracción en formato X/Y: ")
        valor_evaluado = calcular_porcentaje(fraction)
        
        if valor_evaluado is not None:
            print(f"La cantidad de combustible en el tanque es: {valor_evaluado}")
            break

if __name__ == "__main__":
    main()
