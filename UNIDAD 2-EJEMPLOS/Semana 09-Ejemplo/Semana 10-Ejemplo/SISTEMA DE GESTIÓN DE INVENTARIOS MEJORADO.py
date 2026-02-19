# ============================================================
# SISTEMA DE GESTIÓN DE INVENTARIOS MEJORADO
# Ahora utilizamos archivos para almacenar los datos
# y manejar excepciones durante lectura y escritura.
# ============================================================

ARCHIVO = "inventario.txt"


# ------------------------------------------------------------
# Clase Producto
# ------------------------------------------------------------
class Producto:

    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # Setters con validación
    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad

    def set_precio(self, precio):
        if precio >= 0:
            self.__precio = precio

    # Convertir producto a línea de texto para guardar en archivo
    def to_line(self):
        return f"{self.__id},{self.__nombre},{self.__cantidad},{self.__precio}\n"

    # Mostrar producto
    def __str__(self):
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"


# ------------------------------------------------------------
# Clase Inventario
# ------------------------------------------------------------
class Inventario:

    def __init__(self):
        self.productos = []
        self.cargar_desde_archivo()

    # --------------------------------------------------------
    # Guardar todos los productos en el archivo
    # --------------------------------------------------------
    def guardar_en_archivo(self):
        try:
            with open(ARCHIVO, "w") as archivo:
                for p in self.productos:
                    archivo.write(p.to_line())
            print("Inventario guardado correctamente en archivo.")

        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")

        except Exception as e:
            print("Error inesperado al guardar:", e)

    # --------------------------------------------------------
    # Cargar productos desde el archivo al iniciar el programa
    # --------------------------------------------------------
    def cargar_desde_archivo(self):
        try:
            with open(ARCHIVO, "r") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(",")
                    if len(datos) == 4:
                        id_producto = int(datos[0])
                        nombre = datos[1]
                        cantidad = int(datos[2])
                        precio = float(datos[3])
                        producto = Producto(id_producto, nombre, cantidad, precio)
                        self.productos.append(producto)

            print("Inventario cargado desde archivo.")

        except FileNotFoundError:
            # Si el archivo no existe, se crea automáticamente
            open(ARCHIVO, "w").close()
            print("Archivo no encontrado. Se creó uno nuevo.")

        except PermissionError:
            print("No tienes permisos para leer el archivo.")

        except Exception as e:
            print("Error inesperado al cargar archivo:", e)

    # --------------------------------------------------------
    # Agregar producto
    # --------------------------------------------------------
    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("El ID ya existe.")
                return

        self.productos.append(producto)
        self.guardar_en_archivo()
        print("Producto agregado y guardado correctamente.")

    # --------------------------------------------------------
    # Eliminar producto
    # --------------------------------------------------------
    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()
                print("Producto eliminado y archivo actualizado.")
                return
        print("Producto no encontrado.")

    # --------------------------------------------------------
    # Actualizar producto
    # --------------------------------------------------------
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:

                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)

                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)

                self.guardar_en_archivo()
                print("Producto actualizado y cambios guardados.")
                return

        print("Producto no encontrado.")

    # --------------------------------------------------------
    # Buscar producto
    # --------------------------------------------------------
    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos
                       if nombre.lower() in p.get_nombre().lower()]

        if encontrados:
            print("\nProductos encontrados:")
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron productos.")

    # --------------------------------------------------------
    # Mostrar productos
    # --------------------------------------------------------
    def mostrar_productos(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            print("\n LISTA DE PRODUCTOS:")
            for p in self.productos:
                print(p)


# ------------------------------------------------------------
# Menú Principal
# ------------------------------------------------------------
def menu():
    inventario = Inventario()

    while True:
        print("\n===== SISTEMA DE INVENTARIOS MEJORADO =====")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                id_producto = int(input("ID: "))
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(producto)

            elif opcion == "2":
                id_producto = int(input("ID a eliminar: "))
                inventario.eliminar_producto(id_producto)

            elif opcion == "3":
                id_producto = int(input("ID a actualizar: "))
                cantidad = input("Nueva cantidad (Enter para omitir): ")
                precio = input("Nuevo precio (Enter para omitir): ")

                nueva_cantidad = int(cantidad) if cantidad else None
                nuevo_precio = float(precio) if precio else None

                inventario.actualizar_producto(id_producto,
                                               nueva_cantidad,
                                               nuevo_precio)

            elif opcion == "4":
                nombre = input("Nombre a buscar: ")
                inventario.buscar_producto(nombre)

            elif opcion == "5":
                inventario.mostrar_productos()

            elif opcion == "6":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida.")

        except ValueError:
            print("Error: Debe ingresar valores numéricos válidos.")


# Punto de entrada
if __name__ == "__main__":
    menu()
