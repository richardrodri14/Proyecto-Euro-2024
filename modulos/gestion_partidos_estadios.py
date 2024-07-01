# Importar clases y funciones necesarias desde otros módulos
from modelos.equipo import Equipo
from modelos.estadio import Estadio
from utilidades.funciones import pedirOpciones, limpiarConsola, pedirFecha, preguntaSiNo

# Definición de la clase GestionPartidosEstadios
class GestionPartidosEstadios:
    # Inicializador de la clase
    def __init__(self, equipos, estadios, partidos):
        self.equipos = equipos
        self.estadios = estadios
        self.partidos = partidos
    
    # Método para mostrar una lista de partidos
    def mostrarPartidos(self, partidos):
        limpiarConsola()  # Limpiar la consola
        if len(partidos) == 0:
            print("No existen partidos disponibles")
            return
        print(f"Partidos disponibles:")
        for partido in partidos:
            nombre_equipo_local = partido.obtenerEquipo(self.equipos).nombre
            nombre_equipo_visitante = partido.obtenerEquipo(self.equipos, False).nombre
            nombre_estadio = partido.obtenerEstadio(self.estadios).nombre
            print(f"\nPartido Número: {partido.numero}")
            print(f"Equipo Local: {nombre_equipo_local}")
            print(f"Equipo Visitante: {nombre_equipo_visitante}")
            print(f"Grupo: {partido.grupo}")
            print(f"Fecha: {partido.fecha_hora}")
            print(f"Estadio: {nombre_estadio}")

    # Método para gestionar la búsqueda y visualización de partidos y estadios
    def gestionarPartidosEstadios(self):
        limpiarConsola()  # Limpiar la consola
        print("Bienvenido al módulo de Gestión de partidos y estadios")
        # Pedir al usuario que elija una opción de búsqueda
        opcion = pedirOpciones("¿Qué búsqueda desea realizar?", "\nIngrese el número correspondiente a la opción: ", [
            "1. Buscar todos los partidos de un país",
            "2. Buscar todos los partidos que se jugarán en un estadio específico",
            "3. Buscar todos los partidos que se jugarán en una fecha determinada"
        ], "La opción seleccionada no es válida, por favor introduzca una opción válida")

        limpiarConsola()
        if opcion == 1:
            # Buscar partidos por equipo
            lista_equipos = Equipo.obtenerListaEquipos(self.equipos)
            opcion = pedirOpciones(
                "¿Qué país desea seleccionar?", 
                "\nSeleccione el equipo, ingresando el número correspondiente a la opción: ",
                lista_equipos,
                "La opción seleccionada no es válida, por favor introduzca una opción válida"
            )
            equipo = self.equipos[opcion - 1]
            partidos = self.buscarPartidosPorEquipo(equipo.id)
            self.mostrarPartidos(partidos)
        elif opcion == 2:
            # Buscar partidos por estadio
            lista_estadios = Estadio.obtenerListaEstadios(self.estadios)
            opcion = pedirOpciones(
                "¿Qué estadio desea seleccionar?", 
                "\nSeleccione el estadio, ingresando el número correspondiente a la opción: ",
                lista_estadios,
                "La opción seleccionada no es válida, por favor introduzca una opción válida"
            )
            estadio = self.estadios[opcion - 1]
            partidos = self.buscarPartidosPorEstadio(estadio.id)
            self.mostrarPartidos(partidos)
        else:
            # Buscar partidos por fecha
            fecha = pedirFecha("Introduzca la fecha con el formato (YYYY-MM-DD): ", "La fecha introducida no es válida, por favor introduzca una fecha válida")
            partidos = self.buscarPartidosPorFecha(fecha)
            self.mostrarPartidos(partidos)
        # Preguntar si desea realizar otra operación
        opcion = preguntaSiNo("\n¿Desea realizar otra operación? (Sí/No): ")
        if opcion:
            self.gestionarPartidosEstadios()

    # Método para buscar partidos por equipo
    def buscarPartidosPorEquipo(self, id_equipo):
        partidos_pais = []
        for partido in self.partidos:
            if partido.id_equipo_local == id_equipo or partido.id_equipo_visitante == id_equipo:
                partidos_pais.append(partido)
        return partidos_pais
    
    # Método para buscar partidos por estadio
    def buscarPartidosPorEstadio(self, id_estadio):
        partidos_estadio = []
        for partido in self.partidos:
            if partido.id_estadio == id_estadio:
                partidos_estadio.append(partido)
        return partidos_estadio
    
    # Método para buscar partidos por fecha
    def buscarPartidosPorFecha(self, fecha):
        partidos_fecha = []
        for partido in self.partidos:
            if partido.fecha_hora.date() == fecha.date():
                partidos_fecha.append(partido)
        return partidos_fecha
