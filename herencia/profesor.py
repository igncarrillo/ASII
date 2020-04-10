from persona import Persona

class Profesor(Persona):

    def __init__(self,nombre,apellido,cantHijos,titulo):
        Persona.__init__(self,nombre,apellido)
        self.cantHijos=cantHijos
        self.titulo=titulo

    def set_cantHijos(self,cantHijos):
        self.cantHijos=cantHijos

    def set_titulo(self,titulo):
        self.titulo=titulo
    
    def get_cantHijos(self):
        return self.cantHijos

    def get_titulo(self):
        return self.titulo
        
