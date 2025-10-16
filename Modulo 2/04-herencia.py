class Persona:
    # Constructor de clase:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")

class Alumno(Persona):
    pass

class Profesor(Persona):
    
    def __init__(self, nombre, email,esp):
        super().__init__(nombre, email)
        self.especialidad = esp

    def mostrar_profesor(self):
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
        print(f"Especialidad: {self.especialidad}")

alumno1= Alumno("Heinz", "trujillohein@gmail.com")
alumno1.mostrar()

profesor1 = Profesor("Dr. Smith", "smith@gmail.com", "Matemáticas")
profesor1.mostrar_profesor()