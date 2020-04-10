from interfazJPA import InterfazJPA

class EclipseLink(InterfazJPA):

    def __init__(self):
        InterfazJPA.__init__(self)

    def buscar(self):
        print("Busco en la forma eclipseLink")

    def eliminar(self):
        print("Elimino en la forma eclipseLink")

    def guardar(self):
        print("Guardo en al forma eclipse link")