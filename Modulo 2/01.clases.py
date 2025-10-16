#Clases
# Las clases son plantillas para crear objetos. Un objeto tiene propiedades y comportamientos asociados con él. En Python, las clases se crean utilizando la palabra clave `class`.
# Una clase puede contener atributos (variables) y métodos (funciones) que definen el comportamiento del objeto.

class Automovil:
    #Creamos constructor de la clase
    def __init__(self, aa, pl, col, mar):
        self.año = aa        #Atributo año
        self.placa = pl    #Atributo placa
        self.color = col     #Atributo color
        self.marca = mar     #Atributo marca

    #Creamos un metodo
    def encender(self):
        print(f"Encender el automovil {self.marca} {self.placa}")
    def avanzar(self):
        print(f"El automovil {self.marca} {self.placa} esta avanzando.")
    def acelerar(self):
        print(f"El automovil {self.marca} {self.placa} esta acelerando.")
    def frenar(self):
        print(f"El automovil {self.marca} {self.placa} esta frenando.")

#Crear un objeto de la clase Automovil
VW = Automovil(2020, "ABC123", "Rojo", "Volkswagen")
VW.encender()

tico = Automovil(2015, "XYZ789", "Azul", "Kia")
tico.encender()
    