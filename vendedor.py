class Vendedor:
  
    def __init__(self, nombre, rut, telefono):
        self._nombre = nombre
        self._rut = rut
        self._telefono = telefono

    def mostrarDatos(self) -> None:
        
        print(f"Vendedor: {self._nombre} | RUT: {self._rut} | Teléfono: {self._telefono}")

    def calcularComision(self, montoVenta: float) -> float:
       
        if montoVenta >= 5000000:
            return montoVenta * 0.10
        else:
            return montoVenta * 0.05