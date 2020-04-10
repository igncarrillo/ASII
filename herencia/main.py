from persona import Persona
from profesor import Profesor
from alumno import Alumno
import os

os.system("clear")

#definiciones
alumno1=Alumno("59289","Ignacio","Carrillo")
profesor1=Profesor("Alberto","Cortez","1","Ingeniero en Sistemas")

print("Alumno:\n")
print("Nombre:",alumno1.getNombre())
print("Apellido:",alumno1.getApellido())
print("Legajo:",alumno1.get_legajo())
print()
print("Profesor:\n")
print("Nombre:",profesor1.getNombre())
print("Apellido:",profesor1.getApellido())
print("Cantidad de hijos:",profesor1.get_cantHijos())
print("Titulo:",profesor1.get_titulo())
print()