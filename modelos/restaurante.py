from utilidades.funciones import numeroClasificacion

class Restaurante:
    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

    def mostrar(self):
        print(self.nombre)

    def mostrarProductos(self, numeracion = True):
        print("Productos\n")
        for i, producto in enumerate(productos):
            producto.mostrar(i, False)
    
    def obtenerProductoPorIndice(self, indice):
        if (indice > len(self.productos) or indice == 0):
            return None
        return self.productos[indice]

    @staticmethod
    def actualizarProductosRestaurantes(restaurantes, compras):
        for restaurante in restaurantes:
            for producto in restaurante.productos:
                for compra in compras:
                    for pedido in compra.pedidos:
                        if pedido['nombre'] == producto.nombre:
                            producto.unidades -= pedido['cantidad']
                            producto.cantidad += pedido['cantidad']

    @staticmethod
    def obtenerListaRestaurantes(restaurantes, numeracion = True):
        lista = []
        if numeracion:
            for i, restaurante in enumerate(restaurantes):
                elemento = f"{i + 1}. {restaurante.nombre}"
                lista.append(elemento)
        return lista

    def buscarProductoPorNombre(self, nombre):
        productos = []
        for producto in self.productos:
            if producto.nombre == nombre:
                productos.append(producto)
        return productos

    def buscarProductoPorClasificacion(self, clasificacion):
        productos = []
        clasificacion = numeroClasificacion(clasificacion)
        for producto in self.productos:
            if producto.clasificacion == clasificacion:
                productos.append(producto)
        return productos

    def buscarProductoPorPrecio(self, precio_minimo, precio_maximo):
        productos = []
        precio_minimo = float(precio_minimo)
        precio_maximo = float(precio_maximo)
        for producto in self.productos:
            if producto.precio >= precio_minimo and producto.precio <= precio_maximo:
                productos.append(producto)
        return productos