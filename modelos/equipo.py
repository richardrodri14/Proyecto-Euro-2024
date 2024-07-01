class Equipo:
    def __init__(self, id, nombre, codigo_fifa, grupo):
        self.id = id
        self.nombre = nombre
        self.codigo_fifa = codigo_fifa
        self.grupo = grupo

    @staticmethod
    def obtenerListaEquipos(equipos, numeracion = True):
        lista = []
        if numeracion:
            for i, equipo in enumerate(equipos):
                elemento = f"{i + 1}. {equipo.nombre}"
                lista.append(elemento)
        return lista
