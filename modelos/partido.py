from datetime import datetime

class Partido:
    def __init__(self, id, numero, id_equipo_local, id_equipo_visitante, fecha_hora, grupo, id_estadio):
        self.id = id
        self.numero = numero
        self.id_equipo_local = id_equipo_local
        self.id_equipo_visitante = id_equipo_visitante
        self.fecha_hora = datetime.strptime(fecha_hora, '%Y-%m-%d')
        self.grupo = grupo[-1]
        self.id_estadio = id_estadio

    def obtenerEquipo(self, equipos, local = True):
        for equipo in equipos:
            if local:
                if equipo.id == self.id_equipo_local:
                    return equipo
            else:
                if equipo.id == self.id_equipo_visitante:
                    return equipo
        return None

    def obtenerEstadio(self, estadios):
        for estadio in estadios:
            if estadio.id == self.id_estadio:
                return estadio
        return None

    @staticmethod
    def obtenerPartidoPorNumero(partidos, numero):
        if not str.isdigit(str(numero)):
            return None
        for partido in partidos:
            if partido.numero == int(numero):
                return partido
        return None

    @staticmethod
    def obtenerPartidoPorId(partidos, id):
        for partido in partidos:
            if partido.id == id:
                return partido
        return None

    @staticmethod
    def obtenerPartidoConMayorAsistencia(partidos, entradas):
        partido_obtenido = None
        asistencias = 0
        for partido in partidos:
            asistencias_nuevo = 0
            for entrada in entradas:
                if entrada.id_partido == partido.id and entrada.usado:
                    asistencias_nuevo += 1
            if asistencias_nuevo > asistencias:
                asistencias = asistencias_nuevo
                partido_obtenido = partido
        return partido_obtenido

    @staticmethod
    def obtenerPartidoConMayorVenta(partidos, entradas):
        partido_obtenido = None
        ventas = 0
        for partido in partidos:
            ventas_nuevo = 0
            for entrada in entradas:
                if entrada.id_partido == partido.id:
                    ventas_nuevo += 1
            if ventas_nuevo > ventas:
                ventas = ventas_nuevo
                partido_obtenido = partido
        return partido_obtenido
    

    @staticmethod
    def obtenerPartidosPorIDs(partidos, ids_partidos):
        partidos_obtenidos = []
        for id_partido in ids_partidos:
            for partido in partidos:
                if partido.id == id_partido and not partido in partidos_obtenidos:
                    partidos_obtenidos.append(partido)
        return partidos_obtenidos
