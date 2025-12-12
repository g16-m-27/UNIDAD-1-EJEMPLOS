# PROGRAMACIÓN ORIENTADA A OBJETOS USANSO LA TÉCNICA (POO)

class ClimaSemanal:
    def __init__(self):
        self.__temperaturas = []  # Encapsulamiento: atributo privado

    # Método para ingresar datos
    def ingresar_datos(self):
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
            self.__temperaturas.append(temp)

    # Método para calcular el promedio
    def calcular_promedio(self):
        return sum(self.__temperaturas) / len(self.__temperaturas)

    # Polimorfismo (método que podría ser sobrescrito por una clase hija)
    def mostrar_resultado(self):
        print(f"Promedio semanal: {self.calcular_promedio():.2f} °C")


# Es una clase hija que demuestra herencia y polimorfismo
class ClimaExtendido(ClimaSemanal):
    # Sobrescribe método para mostrar resultado
    def mostrar_resultado(self):
        print("+++ RESULTADO DEL CLIMA +++")
        super().mostrar_resultado()

#Se creó una clase llamada ClimaSemanal para representar la información del clima.
#Utilice la tecnica de encapsulamiento la cual se uso  protegiendo sus datos
# con atributos privados y se creó además una clase hija

# Programa principal
def main():
    print("*** PROMEDIO SEMANAL DE TEMPERATURAS (POO) ***")
    clima = ClimaExtendido()   # Uso de herencia y polimorfismo
    clima.ingresar_datos()
    clima.mostrar_resultado()

main()
