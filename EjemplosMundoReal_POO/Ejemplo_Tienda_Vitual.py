# Clase Producto
class Producto:
    def __init__(self, nombre, precio, stock):
        # Atributos del producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def reducir_stock(self, cantidad):
        # Reduce el stock cuando se realiza una compra
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        else:
            return False


# Clase Cliente
class Cliente:
    def __init__(self, nombre):
        # Atributo del cliente
        self.nombre = nombre

    def mostrar_cliente(self):
        return f"Cliente: {self.nombre}"


# Clase Compra
class Compra:
    def __init__(self, cliente, producto, cantidad):
        # Relación entre cliente y producto
        self.cliente = cliente
        self.producto = producto
        self.cantidad = cantidad

    def calcular_total(self):
        # Calcula el total de la compra
        return self.producto.precio * self.cantidad

    def realizar_compra(self):
        # Verifica stock y realiza la compra
        if self.producto.reducir_stock(self.cantidad):
            return f"""
            Compra realizada con éxito
            {self.cliente.mostrar_cliente()}
            Producto: {self.producto.nombre}
            Cantidad: {self.cantidad}
            Total a pagar: ${self.calcular_total()}
            """
        else:
            return "No hay suficiente stock para realizar la compra"


# Programa principal
if __name__ == "__main__":
    # Crear producto
    producto1 = Producto("Televisor Motorola", 550, 5)

    # Crear cliente
    cliente1 = Cliente("Zuleyka Zhune")

    # Crear compra
    compra1 = Compra(cliente1, producto1, 2)

    # Realizar compra
    print(compra1.realizar_compra())
