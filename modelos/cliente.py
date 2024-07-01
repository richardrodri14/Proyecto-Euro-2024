import uuid

class Cliente:
    def __init__(self, nombre, cedula, edad, id = None):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.id = id
        if self.id == None:
            self.id = str(uuid.uuid4())

    @staticmethod
    def obtenerClientePorCedula(clientes, cedula):
        for cliente in clientes:
            if cliente.cedula == cedula:
                return cliente
        return None
