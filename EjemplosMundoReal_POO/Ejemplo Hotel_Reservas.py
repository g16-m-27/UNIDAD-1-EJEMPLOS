# Clase Cliente
class Cliente:
    def __init__(self, nombre, cedula):
        # Atributos del cliente
        self.nombre = nombre
        self.cedula = cedula

    def mostrar_datos(self):
        # Método para mostrar información del cliente
        return f"Cliente: {self.nombre} - Cédula: {self.cedula}"


# Clase Habitacion
class Habitacion:
    def __init__(self, numero, tipo, precio):
        # Atributos de la habitación
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    def reservar(self):
        # Método para reservar la habitación
        if self.disponible:
            self.disponible = False
            return "Habitación reservada con éxito"
        else:
            return "La habitación no está disponible"

    def liberar(self):
        # Método para liberar la habitación
        self.disponible = True


# Clase Reserva
class Reserva:
    def __init__(self, cliente, habitacion, dias):
        # Atributos de la reserva
        self.cliente = cliente
        self.habitacion = habitacion
        self.dias = dias

    def calcular_total(self):
        # Calcula el costo total de la reserva
        return self.dias * self.habitacion.precio

    def confirmar_reserva(self):
        # Confirma la reserva si la habitación está disponible
        mensaje = self.habitacion.reservar()
        if self.habitacion.disponible == False:
            return f"""
            Reserva confirmada
            {self.cliente.mostrar_datos()}
            Habitación: {self.habitacion.numero}
            Días: {self.dias}
            Total a pagar: ${self.calcular_total()}
            """
        else:
            return mensaje


# Programa principal
if __name__ == "__main__":
    # Crear un cliente
    cliente1 = Cliente("Zuleyka Zhune", "0751058736")

    # Crear una habitación
    habitacion1 = Habitacion(101, "Individual", 40)

    # Crear una reserva
    reserva1 = Reserva(cliente1, habitacion1, 3)

    # Confirmar la reserva
    print(reserva1.confirmar_reserva())
