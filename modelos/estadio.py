class Estadio:
    def __init__(self, id, nombre, ciudad, capacidad, restaurantes):
        self.id = id
        self.nombre = nombre
        self.ciudad = ciudad
        self.capacidad = capacidad
        self.restaurantes = restaurantes

    
    @staticmethod
    def obtenerListaEstadios(estadios, numeracion = True):
        lista = []
        if numeracion:
            for i, estadio in enumerate(estadios):
                elemento = f"{i + 1}. {estadio.nombre}"
                lista.append(elemento)
        return lista
