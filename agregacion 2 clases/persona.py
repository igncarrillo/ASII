class Persona():

    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

    def set_nombre(self,nombre):
        self.nombre=nombre
    
    def set_apellido(self,apellido):
        self.apellido=apellido

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido
    
    def agregar(self,refDomicilio):
        self.refDomicilio=refDomicilio

    def get_refDomicilio(self):
        return self.refDomicilio