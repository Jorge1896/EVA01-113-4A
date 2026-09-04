from vehiculo import Vehiculo


class Motocicleta(Vehiculo):

    def __init__(self, patente, marca, modelo, año, precio, cilindrada, tipo):

        super().__init__(patente, marca, modelo, año, precio)

        self.cilindrada = cilindrada
        self.tipo = tipo

    def encenderMotor(self):
        print(f"Encendiendo el motor de la motocicleta ({self.tipo}) con patente {self.patente}...")

    def esDeAltaCilindrada(self):
           
            return self.cilindrada >= 600
    

    
    
   

   

   
