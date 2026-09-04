class Vehiculo:
    
    def __init__(self, patente, marca, modelo, año, precio):
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self._precio = precio  # Atributo privado/protegido según diagrama UML

    def mostrarInfo(self):
        
        print(f"Patente: {self.patente} | Marca: {self.marca} | Modelo: {self.modelo} | Año: {self.año} | Precio: ${self._precio:,.0f}")

    def calcularAniosUso(self, añoActual):
        
        return añoActual - self.año