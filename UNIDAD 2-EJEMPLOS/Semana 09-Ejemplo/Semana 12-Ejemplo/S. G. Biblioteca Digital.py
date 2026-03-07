# ==============================
# Clase Libro
# ==============================
# Representa un libro con título, autor, categoría e ISBN
# Se usa una TUPLA para almacenar título y autor (datos inmutables)

class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # tupla (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def mostrar_info(self):
        return f"Título: {self.info[0]}, Autor: {self.info[1]}, Categoría: {self.categoria}, ISBN: {self.isbn}"


# ==============================
# Clase Usuario
# ==============================
# Representa un usuario con nombre, ID único y lista de libros prestados

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # lista de libros prestados

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def mostrar_libros(self):
        if not self.libros_prestados:
            return "No tiene libros prestados."
        return [libro.info[0] for libro in self.libros_prestados]


# ==============================
# Clase Biblioteca
# ==============================
# Gestiona libros, usuarios y préstamos
# Usa:
# - Diccionario para libros
# - Conjunto para IDs únicos
# - Lista para libros prestados

class Biblioteca:

    def __init__(self):
        self.libros = {}  # diccionario {isbn: objeto_libro}
        self.usuarios = {}
        self.ids_usuarios = set()  # conjunto para IDs únicos

    # ==============================
    # Añadir libro
    # ==============================
    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print("Libro agregado correctamente.")
        else:
            print("El libro ya existe.")

    # ==============================
    # Quitar libro
    # ==============================
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado.")
        else:
            print("Libro no encontrado.")

    # ==============================
    # Registrar usuario
    # ==============================
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print("Usuario registrado.")
        else:
            print("ID de usuario ya existe.")

    # ==============================
    # Eliminar usuario
    # ==============================
    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario eliminado.")
        else:
            print("Usuario no encontrado.")

    # ==============================
    # Prestar libro
    # ==============================
    def prestar_libro(self, isbn, id_usuario):

        if isbn not in self.libros:
            print("Libro no disponible.")
            return

        if id_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return

        libro = self.libros.pop(isbn)
        usuario = self.usuarios[id_usuario]

        usuario.prestar_libro(libro)

        print("Libro prestado correctamente.")

    # ==============================
    # Devolver libro
    # ==============================
    def devolver_libro(self, libro, id_usuario):

        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            usuario.devolver_libro(libro)
            self.libros[libro.isbn] = libro

            print("Libro devuelto correctamente.")

    # ==============================
    # Buscar libros
    # ==============================
    def buscar_libro(self, texto):

        resultados = []

        for libro in self.libros.values():
            if texto.lower() in libro.info[0].lower() \
               or texto.lower() in libro.info[1].lower() \
               or texto.lower() in libro.categoria.lower():

                resultados.append(libro.mostrar_info())

        return resultados

    # ==============================
    # Listar libros prestados
    # ==============================
    def libros_prestados_usuario(self, id_usuario):

        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            return usuario.mostrar_libros()
        else:
            return "Usuario no encontrado."


# ==============================
# PRUEBA DEL SISTEMA
# ==============================

biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("Python Básico", "Juan Pérez", "Programación", "111")
libro2 = Libro("Matemáticas Avanzadas", "Ana López", "Educación", "222")
libro3 = Libro("Historia del Ecuador", "Carlos Ruiz", "Historia", "333")

# Agregar libros
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# Crear usuarios
usuario1 = Usuario("Zuleyka Zhune", 1)
usuario2 = Usuario("Luis", 2)

# Registrar usuarios
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libro
biblioteca.prestar_libro("111", 1)

# Mostrar libros prestados
print("Libros prestados a Zuleyka Zhune:")
print(biblioteca.libros_prestados_usuario(1))

# Buscar libro
print("Buscar 'Historia':")
print(biblioteca.buscar_libro("Historia"))

# Devolver libro
biblioteca.devolver_libro(libro1, 1)

# Mostrar nuevamente
print("Libros prestados después de devolver:")
print(biblioteca.libros_prestados_usuario(1))