class ControladorTour:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar(self):
        while True:
            opcion = self.vista.mostrar_menu()

            if opcion == "1":
                try:
                    nombre, precio, cupos = self.vista.pedir_datos_tour()
                    nuevo_codigo = self.modelo.registrar(nombre, precio, cupos)
                    self.vista.mostrar_mensaje(f"Registrado con el código {nuevo_codigo}.")
                except ValueError:
                    self.vista.mostrar_error("ingrese valores numéricos válidos.")

            elif opcion == "2":
                tours = self.modelo.obtener_todos()
                self.vista.mostrar_tours(tours)

            elif opcion == "3":
                try:
                    codigo, cantidad = self.vista.pedir_datos_reserva()
                    cupos_restantes = self.modelo.reservar_cupos(codigo, cantidad)
                    self.vista.mostrar_mensaje(f"Listo. Quedan {cupos_restantes} cupos.")
                except ValueError as e:
                    if "invalid literal" in str(e):
                        self.vista.mostrar_error("ingrese valores numéricos válidos.")
                    else:
                        self.vista.mostrar_error(e)

            elif opcion == "4":
                self.vista.mostrar_mensaje("Saliendo del programa...")
                break

            else:
                self.vista.mostrar_mensaje("Opción no válida")