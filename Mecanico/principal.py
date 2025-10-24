from modelo_mecanico import Carro, MaquinaRobotica, Mecanico

marca = input("Ingrese la marca del carro: ")
modelo = input("Ingrese el modelo del carro: ")
color = input("Ingrese el color del carro: ")

carro = Carro(marca, modelo, color)
maquina = MaquinaRobotica("MX-2025")
mecanico = Mecanico("Carlos Ramírez")


while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Inspeccionar carro")
    print("2. Encender máquina")
    print("3. Operar máquina")
    print("4. Entregar carro")
    print("5. Salir")
    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            mecanico.inspeccionar_carro(carro)
        case "2":
            maquina.encender()
        case "3":
            tipo = input("Ingrese tipo de operación (repintar / instalar parabrisas / revisar motor): ")
            mecanico.operar_maquina(maquina, carro, tipo)
        case "4":
            mecanico.entregar_carro(carro)
        case "5":
            print("Programa finalizado.")
            break
        case _:
            print("Opción no válida, intenta de nuevo.")


