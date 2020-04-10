from persona import Persona
import os

persona1=Persona("ignacio","carrillo")
persona2=Persona("agus","salomon")
os.system("clear")
print("Listado de Personas:\n")
print("El nombre es:",persona1.getNombre())
print("El apellido es:",persona1.getApellido())
print()
print("El nombre es:",persona2.getNombre())
print("El apellido es:",persona2.getApellido())
print()