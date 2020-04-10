from eclipseLink import EclipseLink
from hibernate import Hibernate
from interfazJPA import InterfazJPA
import os

os.system("clear")
print()
hibernate1=Hibernate()
hibernate1.buscar()
hibernate1.eliminar()
hibernate1.guardar()
print()
eclipseLink1=EclipseLink()
eclipseLink1.buscar()
eclipseLink1.eliminar()
eclipseLink1.guardar()
print()
