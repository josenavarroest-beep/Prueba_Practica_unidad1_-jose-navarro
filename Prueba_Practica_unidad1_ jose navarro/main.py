from modelo import GestorTours
from vista import VistaTour
from controlador import ControladorTour

modelo = GestorTours()
vista = VistaTour()
controlador = ControladorTour(modelo, vista)
controlador.ejecutar()