from domicilio import Domicilio

class Persona():

    def __init__(self,nombre,apellido,numero,calle):
        self.nombre=nombre
        self.apellido=apellido
        self.refDomicilio=Domicilio(calle,numero)

    def set_nombre(self,nombre):
        self.nombre=nombre

    def set_apellido(self,apellido):
        self.apellido=apellido

    def set_refDomicilio(self,refDomicilio):
        self.refDomicilio=refDomicilio
    
    def get_nombre(self):
        return self.nombre
    
    def get_apellido(self):
        return self.apellido
    
    def get_refDomicilio(self):
        return self.refDomicilio
    
