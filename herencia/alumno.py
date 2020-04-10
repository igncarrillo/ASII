from persona import Persona

class Alumno(Persona):

    def __init__(self,legajo,nombre,apellido):
        Persona.__init__(self,nombre,apellido)
        self.legajo=legajo

    def set_legajo(self,legajo):
        self.legajo=legajo

    def get_legajo(self):
        return self.legajo