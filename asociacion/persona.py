
class Persona():

    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

    def setNombre(self,nombre):
        self.nombre=nombre
    
    def setApellido(self,apellido):
        self.apellido=apellido

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def set_refDomicilio(self,referencia):
        self.refDomicilio=referencia
    
    def get_refDomicilio(self):
        return self.refDomicilio