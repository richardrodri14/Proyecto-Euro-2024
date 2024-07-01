import uuid

from utilidades.funciones import convertirClasificacion

class Producto:
    def __init__(self, nombre, cantidad, clasificacion, precio, unidades):
        self.nombre = nombre
        self.cantidad = cantidad
        self.clasificacion = clasificacion
        self.precio = precio
        self.unidades = unidades

    def mostrar(self, numero = 0, mostrarCantidad = True):
        print("")
        if numero != 0:
            print(f"Numero: {numero}")
        print(f"Nombre: {self.nombre}")
        if mostrarCantidad:
            print(f"Cantidad vendida: {self.cantidad}")
        print(f"Clasificacion: {convertirClasificacion(self.clasificacion)}")
        print(f"Precio: {self.precio}")
        print(f"Unidades: {self.unidades}")

