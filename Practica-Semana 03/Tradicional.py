# PROGRAMACIÓN TRADICIONAL

# Esta función es para ingresar las temperaturas de la semana (7 días)
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

# Esta función es para calcular el promedio semanal
def calcular_promedio(temps):
    return sum(temps) / len(temps)

def main():
    print("+++ PROMEDIO SEMANAL DE TEMPERATURAS +++")
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)
    print(f"\nEl promedio semanal es: {promedio:.2f} °C")
# El programa se organiza usando funciones independientes como tambien
# cada función recibe las temperaturas de cada día y otra calcula el promedio.
#No hay clases ni objetos, solo funciones y variables.

# Ejecutar el programa
main()
