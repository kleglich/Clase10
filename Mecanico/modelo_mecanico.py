
class Carro:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.estado = "en espera"

    def recibir_carro(self):
        self.estado = "en revisión"
        print(f"El carro {self.marca} {self.modelo} ha sido recibido para revisión.")

    def preparar_para_trabajo(self):
        self.estado = "en proceso"
        print(f"El carro {self.marca} {self.modelo} está siendo preparado para el trabajo.")

    def finalizar_trabajo(self):
        self.estado = "listo"
        print(f"El carro {self.marca} {self.modelo} está listo para entregarse.")


class MaquinaRobotica:
    def __init__(self, maquina):
        self.maquina = maquina
        self.encendida = False

    def encender(self):
        self.encendida = True
        print(f"La máquina {self.maquina} ha sido encendida.")

    def realizar_operacion(self, carro, tipo_operacion):
        if not self.encendida:
            print("No se puede operar: la máquina está apagada.")
            return

        match tipo_operacion.lower():
            case "repintar":
                print(f"La máquina {self.maquina} pinta el carro {carro.marca} de color {carro.color}.")
                carro.preparar_para_trabajo()
            case "instalar parabrisas":
                print(f"La máquina {self.maquina} instala el parabrisas en el carro {carro.marca}.")
                carro.preparar_para_trabajo()
            case "revisar motor":
                print(f"La máquina {self.maquina} revisa el motor del carro {carro.marca}.")
                carro.preparar_para_trabajo()
            case _:
                print(f"Operación '{tipo_operacion}' no reconocida.")
                return

        carro.finalizar_trabajo()

    def apagar(self):
        self.encendida = False
        print(f"La máquina {self.maquina} ha sido apagada.")


class Mecanico:
    def __init__(self, nombre):
        self.nombre = nombre

    def inspeccionar_carro(self, carro):
        print(f"{self.nombre} inspecciona el carro {carro.marca} {carro.modelo}.")
        carro.recibir_carro()

    def operar_maquina(self, maquina, carro, tipo_operacion):
        print(f"{self.nombre} inicia la operación '{tipo_operacion}'.")
        maquina.realizar_operacion(carro, tipo_operacion)
        maquina.apagar()

    def entregar_carro(self, carro):
        print(f"{self.nombre} entrega el carro {carro.marca} {carro.modelo} al cliente.")

