from persona import Persona
from domicilio import Domicilio
import os

persona1=Persona("Ignacio","Carrillo")
domicilio1=Domicilio("Guardia Vieja","491")
domicilio2=Domicilio("Neuquen","3412")
persona2=Persona("Nicol","Gutierrez")

#asocio el domicilio a la persona
persona1.set_refDomicilio(domicilio1)
persona2.set_refDomicilio(domicilio2)

os.system("clear")
print("Lista de Personas:\n")
print("Nombre:",persona1.getNombre())
print("Apellido:",persona1.getApellido())
print("Domicilio:",persona1.get_refDomicilio().getCalle(),persona1.get_refDomicilio().getNumero())
print()
print("Nombre:",persona2.getNombre())
print("Apellido:",persona2.getApellido())
print("Domicilio:",persona2.get_refDomicilio().getCalle(),persona2.get_refDomicilio().getNumero())
print()
