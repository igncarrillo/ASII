from domicilio import Domicilio
from persona import Persona
import os

persona1=Persona("nacho","carrillo")
domicilio1=Domicilio("guardia vieja","456")
persona1.agregar(domicilio1)
#prueba cambio de datos
#domicilio1.set_calle("neuquen")

os.system("clear")
print("Lista de personas:\n")
print("Nombre:",persona1.get_nombre())
print("Apellido:",persona1.get_apellido())
print("Domicilio:",persona1.get_refDomicilio().get_calle(),persona1.get_refDomicilio().get_numero())