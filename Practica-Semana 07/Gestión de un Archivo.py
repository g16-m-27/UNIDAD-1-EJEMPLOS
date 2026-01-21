class Archivo:
    """
    Clase que representa un archivo simple.En lo cual
    demuestra el uso de constructor y destructor en Python.
    """

    def __init__(self, nombre):
        """
        Constructor de la clase.
        Se ejecuta automáticamente cuando se crea un objeto.
        Inicializa los atributos del objeto.
        """
        self.nombre = nombre
        self.abierto = True
        print(f"El archivo '{self.nombre}' ha sido abierto.")

    def escribir(self, texto):
        """
        Método para simular la escritura en un archivo.
        """
        if self.abierto:
            print(f"Escribiendo en '{self.nombre}': {texto}")
        else:
            print("No se puede escribir, el archivo está cerrado.")

    def cerrar(self):
        """
        Método para cerrar manualmente el archivo.
        """
        if self.abierto:
            self.abierto = False
            print(f"El archivo '{self.nombre}' ha sido cerrado manualmente.")

    def __del__(self):
        """
        Destructor de la clase.
        Este se ejecuta automáticamente cuando el objeto es eliminado
        o cuando el programa finaliza.
        Lo utilizo para liberar recursos.
        """
        if self.abierto:
            print(f"El archivo '{self.nombre}' se cerró automáticamente al destruir el objeto.")
            self.abierto = False


# +.+.+.+.+.+.+.+.+ Uso del programa +.+.+.+.+.+.+.+.+

# Creación del objeto (se activa el constructor)
archivo1 = Archivo("datos.txt")

# Uso de un método de la clase
archivo1.escribir("Hola, este es un ejemplo de constructor y destructor.")

# Eliminación del objeto (se activa el destructor)
del archivo1
