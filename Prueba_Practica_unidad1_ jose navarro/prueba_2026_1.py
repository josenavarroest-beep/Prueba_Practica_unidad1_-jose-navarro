class Tour:
    def __init__(self, codigo, nombre, precio, cupos):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = float(precio)
        self.cupos = int(cupos)

    def reservar(self, cantidad):
        if cantidad <= 0:
            print("Error: la cantidad debe ser mayor que cero.")
            return False
        if cantidad > self.cupos:
            print(f"Error: solo hay {self.cupos} cupos.")
            return False
        self.cupos -= cantidad
        print(f"Listo. Quedan {self.cupos} cupos.")
        return True

    def __str__(self):
        return f"{self.codigo:<8} {self.nombre:<22} ${self.precio:<9.2f} {self.cupos:<6}"


def buscar_tour(tours, codigo):
    for tour in tours:
        if tour.codigo == codigo:
            return tour
    return None


def main():
    tours = [
        Tour(1, "Centro histórico", 15.00, 20),
        Tour(2, "El Cajas", 35.00, 12),
    ]

    while True:
        print("\n--- Tours Cuenca Colonial ---")
        print("1. Registrar tour")
        print("2. Mostrar tours")
        print("3. Reservar cupos")
        print("4. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Opción no válida")
            continue

        if opcion == 1:
            nombre = input("Nombre del tour: ").strip()
            try:
                precio = float(input("Precio: "))
                cupos = int(input("Cupos: "))
            except ValueError:
                print("Error: ingrese valores numéricos válidos.")
                continue

            nuevo_codigo = len(tours) + 1
            nuevo_tour = Tour(nuevo_codigo, nombre, precio, cupos)
            tours.append(nuevo_tour)
            print(f"Registrado con el código {nuevo_codigo}.")

        elif opcion == 2:
            if not tours:
                print("No hay tours registrados.")
            else:
                print(f"{'Código':<8} {'Nombre':<22} {'Precio':<10} {'Cupos':<6}")
                print("-" * 50)
                for tour in tours:
                    print(tour)

        elif opcion == 3:
            try:
                codigo = int(input("Código del tour: "))
            except ValueError:
                print("Error: no existe ese código.")
                continue

            tour = buscar_tour(tours, codigo)
            if tour is None:
                print("Error: no existe ese código.")
                continue

            try:
                cantidad = int(input("Cantidad de cupos a reservar: "))
            except ValueError:
                print("Error: cantidad inválida.")
                continue

            tour.reservar(cantidad)

        elif opcion == 4:
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()