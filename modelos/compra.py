import uuid

class Compra:
    def __init__(self, id_cliente, pedidos, descuento, id = None):
        self.id_cliente = id_cliente
        self.pedidos = pedidos
        self.descuento = descuento
        self.id = id
        if self.id == None:
            self.id = str(uuid.uuid4())
    
    @staticmethod
    def obtenerPedidosPorCompras(pedidos, compras):
        pedidos_obtenidos = []
        for compra in compras:
            pedidos_obtenidos += compra.pedidos
        return pedidos_obtenidos

    def obtenerIVA(self):
        return self.obtenerSubtotal() * .16

    def obtenerPrecioTotal(self):
        return self.obtenerSubtotal() + self.obtenerIVA() - self.descuento

    def obtenerSubtotal(self):
        subtotal = 0
        for pedido in self.pedidos:
            subtotal += pedido['precio']
        return subtotal

    

    