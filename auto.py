from vehiculo import Vehiculo


class Auto(Vehiculo):

    def __init__(self, patente, marca, modelo, año, precio,
        numPuertas, combustible):

        super().__init__(patente, marca, modelo, año, precio)

        self.numPuertas = numPuertas
        self.combustible = combustible


    def abrirMaletero(self):
        print(f"Abriendo el maletero del auto patente {self.patente}...")

    def tieneAireAcondicionado(self):

        return True
