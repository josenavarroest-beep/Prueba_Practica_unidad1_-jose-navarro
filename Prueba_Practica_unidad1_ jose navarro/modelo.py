class Tour:
    def __init__(self, codigo, nombre, precio, cupos):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = float(precio)
        self.cupos = int(cupos)

    def reservar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("la cantidad debe ser mayor que cero.")
        if cantidad > self.cupos:
            raise ValueError(f"solo hay {self.cupos} cupos.")
        self.cupos -= cantidad
        return self.cupos

    def __str__(self):
        return f"{self.codigo:<8} {self.nombre:<22} ${self.precio:<9.2f} {self.cupos:<6}"


class GestorTours:
    def __init__(self):
        self.tours = [
            Tour(1, "Centro histórico", 15.00, 20),
            Tour(2, "El Cajas", 35.00, 12),
        ]

    def registrar(self, nombre, precio, cupos):
        nuevo_codigo = len(self.tours) + 1
        nuevo_tour = Tour(nuevo_codigo, nombre, precio, cupos)
        self.tours.append(nuevo_tour)
        return nuevo_codigo

    def buscar(self, codigo):
        for tour in self.tours:
            if tour.codigo == codigo:
                return tour
        return None

    def reservar_cupos(self, codigo, cantidad):
        tour = self.buscar(codigo)
        if tour is None:
            raise ValueError("no existe ese código.")
        return tour.reservar(cantidad)

    def obtener_todos(self):
        return self.tours