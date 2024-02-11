class Producto:
    def __init__(self, nombre, precio, año):
        self.nombre = nombre
        self.precio = precio
        self.año = año

    def __str__(self):
        return f"{self.nombre} - Año: {self.año} - Precio: ${self.precio}"


class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_lista(self):
        if not self.productos:
            print("El catálogo está vacío.")
        else:
            print("Lista de productos:")
            for producto in self.productos:
                print(producto)

    def filtrar_por_año(self, año):
        productos_filtrados = [producto for producto in self.productos if producto.año == año]
        if productos_filtrados:
            print(f"Productos del año {año}:")
            for producto in productos_filtrados:
                print(producto)
        else:
            print(f"No hay productos del año {año} en el catálogo.")

    def buscar_por_nombre(self, nombre):
        productos_encontrados = [producto for producto in self.productos if nombre.lower() in producto.nombre.lower()]
        if productos_encontrados:
            print(f"Productos que contienen '{nombre}' en el nombre:")
            for producto in productos_encontrados:
                print(producto)
        else:
            print(f"No se encontraron productos con '{nombre}' en el nombre en el catálogo.")


# Ejemplo de uso:
catalogo = Catalogo()

producto1 = Producto("Batería de coche", 120, 2022)
producto2 = Producto("Filtro de aceite", 15, 2023)
producto3 = Producto("Llantas deportivas", 300, 2022)

catalogo.agregar_producto(producto1)
catalogo.agregar_producto(producto2)
catalogo.agregar_producto(producto3)

catalogo.mostrar_lista()

catalogo.filtrar_por_año(2022)

catalogo.buscar_por_nombre("Filtro")
