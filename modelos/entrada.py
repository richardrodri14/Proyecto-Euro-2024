from utilidades.funciones import convertirEntradaInt

import uuid


class Entrada:
    def __init__(self, id_cliente, id_partido, tipo, asiento, precio, descuento, codigo = None):
        self.id_cliente = id_cliente
        self.id_partido = id_partido
        self.tipo = tipo
        self.asiento = asiento
        self.precio = precio
        self.descuento = descuento
        self.usado = False
        self.codigo = codigo
        if self.codigo == None:
            self.codigo = str(uuid.uuid4())

    def obtenerSubtotal(self):
        return self.precio - self.descuento

    def obtenerIVA(self):
        return self.obtenerSubtotal() * .16

    def obtenerPrecioTotal(self):
        return self.obtenerSubtotal() + self.obtenerIVA()

    @staticmethod
    def obtenerEntradasPorIdCliente(entradas, id_cliente):
        entradas_cliente = []
        for entrada in entradas:
            if entrada.id_cliente == id_cliente:
                entradas_cliente.append(entrada)
        return entradas_cliente
    
    @staticmethod
    def obtenerEntradasPorTipo(entradas, tipo):
        entradas_tipo = []
        if isinstance(tipo, str):
            tipo = convertirEntradaInt(tipo)
        for entrada in entradas:
            if entrada.tipo == tipo:
                entradas_tipo.append(entrada)
        return entradas_tipo