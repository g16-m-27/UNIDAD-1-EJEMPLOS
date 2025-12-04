#Animales
class Animal:

    def __init__(self, nombre, energia, fuerza, defensa):
        self._nombre = nombre
        self._energia = energia
        self._fuerza = fuerza
        self._defensa = defensa

    def mostrar_info(self):
        print(f"\nAnimal: {self._nombre}")
        print(f"·Energía: {self._energia}")
        print(f"·Fuerza: {self._fuerza}")
        print(f"·Defensa: {self._defensa}")

    def esta_vivo(self):
        return self._energia > 0

    def recibir_daño(self, cantidad):
        self._energia -= cantidad
        if self._energia < 0:
            self._energia = 0

    def ataque_especial(self, enemigo):
        pass

    def atacar(self, enemigo):
        daño = self._fuerza - enemigo._defensa
        if daño < 0:
            daño = 0

        enemigo.recibir_daño(daño)
        print(f"{self._nombre} usa ataque básico e inflige {daño} a {enemigo._nombre}")

#Animal 1
class Perro(Animal):

    def __init__(self, nombre, energia, fuerza, defensa, mordida):
        super().__init__(nombre, energia, fuerza, defensa)
        self.mordida = mordida

    def ataque_especial(self, enemigo):
        daño = (self._fuerza * self.mordida) - enemigo._defensa
        if daño < 0:
            daño = 0

        enemigo.recibir_daño(daño)
        print(f"{self._nombre} usa MORDEDURA y hace {daño} de daño a {enemigo._nombre}")

#Animal 2
class Gato(Animal):

    def __init__(self, nombre, energia, fuerza, defensa, garra):
        super().__init__(nombre, energia, fuerza, defensa)
        self.garra = garra

    def ataque_especial(self, enemigo):
        daño = (self._fuerza * self.garra) - enemigo._defensa
        if daño < 0:
            daño = 0

        enemigo.recibir_daño(daño)
        print(f"{self._nombre} usa ZARPA AGUDA y hace {daño} de daño a {enemigo._nombre}")

# Combate

def combate(animal_1, animal_2):
    print("\n====================== INICIO DEL COMBATE ======================")

    for turno in range(1, 3):  # Solo 2 rounds
        print(f"\n====================== Round {turno} ======================")

        # Animal 1
        print(f"\n>>> Acción de {animal_1._nombre}:")
        if turno == 1:
            animal_1.atacar(animal_2)
        else:
            animal_1.ataque_especial(animal_2)

        if not animal_2.esta_vivo():
            break

        # Animal 2
        print(f"\n>>> Acción de {animal_2._nombre}:")
        if turno == 1:
            animal_2.atacar(animal_1)
        else:
            animal_2.ataque_especial(animal_1)

        if not animal_1.esta_vivo():
            break

    print("\n====================== FIN DEL COMBATE ======================")

    if animal_1.esta_vivo() and animal_2.esta_vivo():
        print("¡Fin del combate! Ambos siguen con vida.")
    elif animal_1.esta_vivo():
        print(f"¡{animal_1._nombre} es el ganador!")
    else:
        print(f"¡{animal_2._nombre} es el ganador!")


perro = Perro("Rex", 80, 12, 5, mordida=3)
gato = Gato("Luna", 70, 10, 4, garra=4)

perro.mostrar_info()
gato.mostrar_info()

combate(perro, gato)