"""
Realice un programa que calcula el área de un rectángulo.
En la cual solicita al usuario el largo y el ancho para luego realizar el cálculo
y muestrar el resultado en pantalla.
"""

# Solicitar datos al usuario, usamos float
largo = float(input("Ingrese el largo del rectángulo: "))
ancho = float(input("Ingrese el ancho del rectángulo: "))

# Cálculo del área
area_rectangulo = largo * ancho

# Variable booleana para verificar si el área es mayor a 0
area_valida = area_rectangulo > 0

# Mostrar resultados
print("\n--- RESULTADOS ---")
print(f"Largo: {largo}")
print(f"Ancho: {ancho}")
print(f"Área del rectángulo: {area_rectangulo}")

# Condición usando boolean
if area_valida:
    print("El área calculada es válida.")
else:
    print("El área no es válida.")
