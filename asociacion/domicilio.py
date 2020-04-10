class Domicilio():

    def __init__(self,calle,numero):
        self.calle=calle
        self.numero=numero

    def setCalle(self,calle):
        self.calle=calle

    def setNumero(self,numero):
        self.numero=numero
    
    def getCalle(self):
        return self.calle

    def getNumero(self):
        return self.numero
        