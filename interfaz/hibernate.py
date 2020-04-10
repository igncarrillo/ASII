from interfazJPA import InterfazJPA

class Hibernate(InterfazJPA):
    def __init__(self):
        InterfazJPA.__init__(self)

    def buscar(self):
        print("Busco en la forma de hibernate")

    def eliminar(self):
        print("Elimino en la forma de hibernate")

    def guardar(self):
        print("Guardo en la forma de hibernate")