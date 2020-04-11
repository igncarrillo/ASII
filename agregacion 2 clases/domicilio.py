class Domicilio():

    def __init__(self,calle,numero):
        self.calle=calle
        self.numero=numero

    def set_calle(self,calle):
        self.calle=calle

    def set_numero(self,numero):
        self.numero=numero

    def get_calle(self):
        return self.calle

    def get_numero(self):
        return self.numero
