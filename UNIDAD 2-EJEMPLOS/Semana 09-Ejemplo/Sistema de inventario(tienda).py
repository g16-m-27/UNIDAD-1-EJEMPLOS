# ============================================================
# SISTEMA DE GESTIÓN DE INVENTARIOS
# Autor: Zhune Zuleyka
# Descripción:Es un sistema tipo inventario de una tienda para poder añadir,
# actualizar, eliminar y buscar productos utilizando esta estructura de datos.
# ============================================================

# ------------------------------------------------------------
# Clase Producto
# Representa un producto individual dentro del inventario.
# Cada producto tiene un ID único, nombre, cantidad y precio.
# ------------------------------------------------------------
class Producto:

    # Constructor: inicializa los atributos del producto
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Uso atributos privados (__) para aplicar encapsulamiento
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # ---------------- GETTERS ----------------
    # Permiten acceder a los atributos privados de forma controlada

    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # ---------------- SETTERS ----------------
    # Permite modificar los atributos con validación

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        # Validación: no se permite cantidad negativa
        if cantidad >= 0:
            self.__cantidad = cantidad
        else:
            print("La cantidad no puede ser negativa.")

    def set_precio(self, precio):
        # Validación: no se permite precio negativo
        if precio >= 0:
            self.__precio = precio
        else:
            print("El precio no puede ser negativo.")

    # Método especial que permite mostrar el objeto como texto
    def __str__(self):
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"


# ------------------------------------------------------------
# Clase Inventario
# Administra una lista de productos.
# Contiene los métodos principales del sistema.
# ------------------------------------------------------------
class Inventario:

    # Constructor: Este crea una lista vacía para almacenar productos
    def __init__(self):
        self.productos = []

    # --------------------------------------------------------
    # Método para agregar un producto
    # Se verifica que el ID sea único antes de agregarlo
    # --------------------------------------------------------
    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: El ID ya existe.")
                return
        self.productos.append(producto)
        print("Producto agregado correctamente.")

    # --------------------------------------------------------
    # Método para eliminar un producto por su ID
    # --------------------------------------------------------
    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado correctamente.")
                return
        print("Producto no encontrado.")

    # --------------------------------------------------------
    # Método para actualizar cantidad o precio
    # Se puede actualizar uno o ambos valores
    # --------------------------------------------------------
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:

                # Solo actualiza si el usuario ingresó un valor
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)

                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)

                print("Producto actualizado correctamente.")
                return

        print("Producto no encontrado.")

    # --------------------------------------------------------
    # Método para buscar productos por nombre
    # Permite coincidencias parciales (ej: "lap" encuentra "laptop")
    # --------------------------------------------------------
    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos
                       if nombre.lower() in p.get_nombre().lower()]

        if encontrados:
            print("\nProductos encontrados:")
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    # --------------------------------------------------------
    # Método para mostrar todos los productos del inventario
    # --------------------------------------------------------
    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("\nLISTA DE PRODUCTOS:")
            for p in self.productos:
                print(p)


# ------------------------------------------------------------
# Función principal (Menú interactivo)
# Permite al usuario interactuar con el sistema
# ------------------------------------------------------------
def menu():

    # Se crea una instancia del inventario
    inventario = Inventario()

    # Bucle infinito hasta que el usuario (nosotros) decida salir
    while True:
        print("\n===== SISTEMA DE GESTIÓN DE INVENTARIOS =====")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        # ---------------- AGREGAR ----------------
        if opcion == "1":
            try:
                id_producto = int(input("Ingrese ID: "))
                nombre = input("Ingrese nombre: ")
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))

                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(producto)

            except ValueError:
                print("Error: Debe ingresar valores numéricos válidos.")

        # ---------------- ELIMINAR ----------------
        elif opcion == "2":
            try:
                id_producto = int(input("Ingrese ID del producto a eliminar: "))
                inventario.eliminar_producto(id_producto)
            except ValueError:
                print("ID inválido.")

        # ---------------- ACTUALIZAR ----------------
        elif opcion == "3":
            try:
                id_producto = int(input("Ingrese ID del producto a actualizar: "))

                cantidad = input("Nueva cantidad (Enter para omitir): ")
                precio = input("Nuevo precio (Enter para omitir): ")

                # Si el usuario deja vacío, no se actualiza ese campo
                nueva_cantidad = int(cantidad) if cantidad else None
                nuevo_precio = float(precio) if precio else None

                inventario.actualizar_producto(id_producto,
                                               nueva_cantidad,
                                               nuevo_precio)

            except ValueError:
                print("Datos inválidos.")

        # ---------------- BUSCAR ----------------
        elif opcion == "4":
            nombre = input("Ingrese nombre a buscar: ")
            inventario.buscar_producto(nombre)

        # ---------------- MOSTRAR ----------------
        elif opcion == "5":
            inventario.mostrar_productos()

        # ---------------- SALIR ----------------
        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


# ------------------------------------------------------------
# Punto de entrada del programa
# Esto asegura que el menú solo se ejecute si el archivo
# se ejecuta directamente y no si se importa como módulo.
# ------------------------------------------------------------
if __name__ == "__main__":
    menu()

