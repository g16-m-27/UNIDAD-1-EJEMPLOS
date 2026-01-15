# Clase base Producto
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.__precio = precio  # Atributo encapsulado (privado)

    # Utilizamos método para obtener el precio (encapsulación)
    def get_precio(self):
        return self.__precio

    # Utilizamos método para modificar el precio (encapsulación)
    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El precio debé ser mayor que cero")

    # Método que será sobrescrito (polimorfismo)
    def calcular_precio_final(self):
        return self.__precio

    def mostrar_info(self):
        print(f"Producto: {self.nombre} | Precio: ${self.__precio}")


# Clase derivada Producto Electronico (herencia)
class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, garantia):
        super().__init__(nombre, precio)
        self.garantia = garantia

    # Polimorfismo: sobrescritura del método
    def calcular_precio_final(self):
        # Se aplica un impuesto del 12%
        impuesto = super().calcular_precio_final() * 0.12
        return super().calcular_precio_final() + impuesto

    def mostrar_info(self):
        print(
            f"Producto Electrónico: {self.nombre} | Garantía: {self.garantia} meses | Precio final: ${self.calcular_precio_final():.2f}")


# Programa principal
if __name__ == "__main__":
    # Creación de objetos
    producto1 = Producto("Cuaderno", 3.50)
    producto2 = ProductoElectronico("Laptop", 800, 12)

    # Uso de métodos
    producto1.mostrar_info()
    print("Precio final:", producto1.calcular_precio_final())

    print()

    producto2.mostrar_info()
