from persona import Persona
import os

persona1=Persona("nacho","carrillo","guardia vieja","492")
persona2=Persona("carlos","hernandez","neuquen","345")

os.system("clear")
print("Lista de personas:\n")
print("nombre:",persona1.get_nombre())
print("apellido:",persona1.get_apellido())
print("direccion:",persona1.get_refDomicilio().get_calle(),persona1.get_refDomicilio().get_numero())
print()

#persona2.set_refDomicilio(persona1.get_refDomicilio())
#prueba para cambiar parametros, entender funcion objetos

print("Lista de personas:\n")
print("nombre:",persona2.get_nombre())
print("apellido:",persona2.get_apellido())
print("direccion:",persona2.get_refDomicilio().get_calle(),persona2.get_refDomicilio().get_numero())
print()