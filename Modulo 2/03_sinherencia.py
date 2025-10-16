class Alumno:
    # Constructor de clase:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")


class Profesor:

    # Constructor de clase:
    def __init__(self, nombre, email, especialidad):
        self.nombre = nombre
        self.email = email
        self.especialidad = especialidad

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
        print(f"Especialidad: {self.especialidad}")

profesor1 = Profesor("Dr. Smith", "smith@gmail.com", "Matemáticas")
profesor1.mostrar()

alumno1= Alumno ("Heinz", "trujillohein@gmail.com")
alumno1.mostrar()