class VistaTour:
    def mostrar_menu(self):
        print("\n--- Tours Cuenca Colonial ---")
        print("1. Registrar tour")
        print("2. Mostrar tours")
        print("3. Reservar cupos")
        print("4. Salir")
        return input("Seleccione una opción: ").strip()

    def pedir_datos_tour(self):
        nombre = input("Nombre del tour: ").strip()
        precio = float(input("Precio: "))
        cupos = int(input("Cupos: "))
        return nombre, precio, cupos

    def pedir_datos_reserva(self):
        codigo = int(input("Código del tour: "))
        cantidad = int(input("Cantidad de cupos a reservar: "))
        return codigo, cantidad

    def mostrar_tours(self, tours):
        if not tours:
            self.mostrar_mensaje("No hay tours registrados.")
        else:
            print(f"{'Código':<8} {'Nombre':<22} {'Precio':<10} {'Cupos':<6}")
            print("-" * 50)
            for tour in tours:
                print(tour)

    def mostrar_mensaje(self, mensaje):
        print(mensaje)

    def mostrar_error(self, error):
        print(f"Error: {error}")