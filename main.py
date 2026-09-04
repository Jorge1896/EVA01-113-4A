from auto import Auto
from motocicleta import Motocicleta
from vendedor import Vendedor
from automotora import Automotora


def main():

    # Crear automotora
    automotora = Automotora("Bruno Fritz Automotriz")

    # Crear 2 automóviles
    auto1 = Auto("BCHZ42", "Toyota", "Corolla", 2020,6000000, 4, "Gasolina")
    auto2 = Auto("BGS72", "Honda", "Civic", 2019, 4000000, 4, "Diesel")

    # Crear motocicleta
    moto1 = Motocicleta("AHS412", "Yamaha", "MT-07", 2021, 3000000, 689, "Deportiva")


    # Agregar vehículos a la automotora
    automotora.agregarVehiculo(auto1)
    automotora.agregarVehiculo(auto2)
    automotora.agregarVehiculo(moto1)

    # Mostrar vehículos
    print("===== VEHÍCULOS DE LA AUTOMOTORA =====")
    automotora.mostrarVehiculos()



    # Probar métodos de un Auto
    print("\n===== AUTO =====")
    auto1.mostrarInfo()
    auto1.abrirMaletero()
    print(f"¿Tiene aire acondicionado?: {'Sí' if auto1.tieneAireAcondicionado() else 'No'}")



    # Calcular años de uso del auto
    AÑO_ACTUAL = 2026
    anios_auto1 = auto1.calcularAniosUso(AÑO_ACTUAL)
    print(f"Años de uso del auto patente {auto1.patente} ({auto1.año}): {anios_auto1} años.")


    # Probar métodos de Motocicleta
    print("\n===== MOTOCICLETA =====")
    moto1.mostrarInfo()
    moto1.encenderMotor()
    print(f"¿Es de alta cilindrada ?: {'Sí' if moto1.esDeAltaCilindrada() else 'No'}")


    # Calcular años de uso de la motocicleta
    anios_moto1 = moto1.calcularAniosUso(AÑO_ACTUAL)
    print(f"Años de uso de la moto patente {moto1.patente} ({moto1.año}): {anios_moto1} años.")
    
   


    # Crear vendedor
    vendedor1 = Vendedor("Juan Pérez", "12.345.678-9", "987654321")
    # vendedor1 = Vendedor(
    #     "Juan Pérez",
    #     "12.345.678-9",
    #     "987654321"
    # )

    print("\n===== VENDEDOR =====")
    print("Datos del vendedor:")
    vendedor1.mostrarDatos()

    venta_alta = 6000000
    comision_alta = vendedor1.calcularComision(venta_alta)
    print(f"Venta: ${venta_alta:,.0f} -> Comisión (10%): ${comision_alta:,.0f}")



    

if __name__ == "__main__":
    main()

