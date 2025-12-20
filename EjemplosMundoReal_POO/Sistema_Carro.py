# Clase Carro
class Carro:
    def __init__(self, marca, modelo, anio, combustible):
        # Atributos del carro
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.combustible = combustible  # Nivel de combustible en litros
        self.encendido = False

    def encender(self):
        # Método para encender el carro
        if self.combustible > 0:
            self.encendido = True
            return "El carro ha sido encendido"
        else:
            return "No se puede encender el carro: combustible insuficiente"

    def apagar(self):
        # Método para apagar el carro
        self.encendido = False
        return "El carro ha sido apagado"

    def conducir(self, kilometros):
        # Método para simular la conducción del carro
        if self.encendido and self.combustible > 0:
            consumo = kilometros * 0.1  # Consumo estimado por kilómetro
            if consumo <= self.combustible:
                self.combustible -= consumo
                return f"Condujo {kilometros} km. Combustible restante: {self.combustible:.2f} litros"
            else:
                return "No hay suficiente combustible para recorrer esa distancia"
        else:
            return "El carro debe estar encendido y con combustible"

    def mostrar_estado(self):
        # Muestra el estado actual del carro
        estado = "Encendido" if self.encendido else "Apagado"
        return f"""
        Carro: {self.marca} {self.modelo} ({self.anio})
        Estado: {estado}
        Combustible: {self.combustible:.2f} litros
        """


# Programa principal
if __name__ == "__main__":
    # Crear un objeto de la clase Carro
    carro1 = Carro("Toyota", "Corolla", 2022, 20)

    # Encender el carro
    print(carro1.encender())

    # Conducir el carro
    print(carro1.conducir(50))

    # Mostrar estado del carro
    print(carro1.mostrar_estado())

    # Apagar el carro
    print(carro1.apagar())
