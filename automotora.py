class Automotora:

    def __init__(self, nombre):
        self.nombre = nombre
        self.vehiculos = []

    def agregarVehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def mostrarVehiculos(self):
        print(f"Automotora: {self.nombre}")
        print(f"Vehículos registrados: {len(self.vehiculos)}")

        for vehiculo in self.vehiculos:
            vehiculo.mostrarInfo()
            print("--------------------")