from modelos.equipo import Equipo
from modelos.estadio import Estadio
from utilidades.funciones import pedirOpciones, limpiarConsola, pedirFecha, preguntaSiNo

class GestionEstadisticas:
    def __init__(self, equipos, restaurantes, estadios, partidos, clientes, compras):
        self.equipos = equipos
        self.restaurantes = restaurantes
        self.estadios = estadios
        self.partidos = partidos
        self.clientes = clientes
        self.compras = compras

    def gestionarEstadisticas(self):
        limpiarConsola()
        print("Bienvenido al modulo de Indicadores de gestión (Estadísticas)")
        opcion = pedirOpciones("¿Que desea buscar?", "\nIngrese el numero correspondiente a la opcion: ", [
			"1. Promedio de gasto de un cliente VIP en un partido (ticket + restaurante)",
			"2. Asistencia a los partidos de mejor a peor",
			"3. Partido con mayor asistencia",
            "4. Partido con mayor boletos vendidos",
            "5. Top 3 productos más vendidos en el restaurante",
            "6. Top 3 de clientes (clientes que más compraron boletos)"
		], "La opcion seleccionada no es valida, por favor introduzca una opcion valida")

        limpiarConsola()
        if opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass    
        else:
            pass

