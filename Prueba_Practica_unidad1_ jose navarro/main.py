from modelo import GestorTours
from vista import VistaTour
from controlador import ControladorTour


def main():
    modelo = GestorTours()
    vista = VistaTour()
    controlador = ControladorTour(modelo, vista)
    controlador.ejecutar()


if __name__ == "__main__":
    main()