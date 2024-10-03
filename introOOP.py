class Persona:
    def __init__(self, nombre, edad, genero, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.ocupacion = ocupacion

    # Método 1: Saludar
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre}."

    # Método 2: Cumplir años
    def cumplir_anios(self):
        self.edad += 1
        return f"Ahora tengo {self.edad} años."

    # Método 3: Cambiar de ocupación
    def cambiar_ocupacion(self, nueva_ocupacion):
        self.ocupacion = nueva_ocupacion
        return f"Ahora soy {self.ocupacion}."

    # Método 4: Describir a la persona
    def describir(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}, Ocupación: {self.ocupacion}"

    # Método 5: Saber si es mayor de edad
    def es_mayor_de_edad(self):
        return self.edad >= 18

    #Pasar saludo
    def saludarA(self, nombreOtraPersona):
        return f"Hola, {self.nombre}, te manda saludar {nombreOtraPersona}."



# Crear una instancia de la clase Persona
persona1 = Persona(nombre="Juan", edad=19, genero="Hombre", ocupacion="Estudiante")
persona2 = Persona(nombre="Victor", edad=10, genero="Hombre", ocupacion="Docente")
persona3 = Persona(nombre="Brenda", edad=21, genero="Mujer", ocupacion="Ingeniera")

print(persona1.saludarA(persona2.nombre))



