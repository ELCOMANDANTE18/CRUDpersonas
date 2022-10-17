class Persona:
    def __init__(self, dni = 1, apellido = "Fernandez", nombre = "Alberto"):        
        "Parametro obligatorio"
        self.dni = dni
        self.apellido = apellido 
        self.nombre = nombre 
    def __repr__(self):
        return  f'persona: {self.dni} - {self.apellido} , {self.nombre}'  

    def input(self):
        self.documento = int(input('Ingrese documento: '))
        self.apellido = input('Ingrese apellido: ')
        self.nombre = input('Ingrese nombre: ')  
class PersonaService:
    def input(self,persona = Persona()):
        persona.documento = int(input("Ingrse DNI "))
        persona.apellido = input("Ingrese Apellido ")
        persona.nombre = input("Ingrese Nombre ")

persona = Persona()
personaService = PersonaService()
personaService.input(persona)
print(persona)


persona = Persona()
