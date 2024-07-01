from modelos.restaurante import Restaurante
from modulos.gestion_partidos_estadios import GestionPartidosEstadios
from modulos.gestion_venta_entradas import GestionVentaEntradas
from modulos.gestion_asistencia_partidos import GestionAsistenciaPartidos
from modulos.gestion_restaurantes import GestionRestaurantes
from modulos.gestion_venta_restaurantes import GestionVentaRestaurantes
from utilidades.datos import cargarDatosAPI, cargarDatosArchivos
from utilidades.funciones import mostrarTodo, pedirOpciones, limpiarConsola

if __name__ == '__main__':
    # Se cargan los datos de las APIs y archivos
    equipos, estadios, partidos = cargarDatosAPI()  # Se cargan datos de equipos, estadios y partidos
    clientes, compras, entradas = cargarDatosArchivos()  # Se cargan datos de clientes, compras y entradas

    # Se crea una lista para almacenar los restaurantes
    restaurantes = []

    # Se recorren los estadios y se agregan los restaurantes a la lista
    for estadio in estadios:
        for restaurante in estadio.restaurantes:
            restaurantes.append(restaurante)

    # Se actualiza la información de productos de los restaurantes
    Restaurante.actualizarProductosRestaurantes(restaurantes, compras)

    # Se crean instancias de las clases de gestión
    gestion_partidos_estadios = GestionPartidosEstadios(equipos, estadios, partidos)
    gestion_venta_entradas = GestionVentaEntradas(equipos, estadios, partidos, entradas, clientes)
    gestion_asistencia_partidos = GestionAsistenciaPartidos(entradas)
    gestion_restaurantes = GestionRestaurantes(estadios)
    gestion_venta_restauntes = GestionVentaRestaurantes(estadios, restaurantes, partidos, clientes, compras, entradas)

    while True:
        # Se limpia la consola
        limpiarConsola()

        # Se muestra un mensaje de bienvenida
        print("Bienvenido al sistema gestor de la Eurocopa Alemania 2024")

        # Se solicita la opción al usuario
        opcion = pedirOpciones(
            "¿Cual modulo desea utilizar?",
            "\nSeleccione el modulo, ingresando el numero correspondiente a la opcion: ",
            [
                "1. Gestión de partidos y estadios",
                "2. Gestión de venta de entradas",
                "3. Gestión de asistencia a partidos",
                "4. Gestión de restaurantes",
                "5. Gestión de venta de restaurantes",
                "6. Indicadores de gestión (Estadísticas)",
                "7. Salir"
            ],
            "La opcion seleccionada no es valida, por favor introduzca una opcion valida"
        )

        # Se limpia la consola
        limpiarConsola()

        # Se evalúa la opción seleccionada
        if opcion == 1:
            # Se gestionan los partidos y estadios
            gestion_partidos_estadios.gestionarPartidosEstadios()
        elif opcion == 2:
            # Se gestiona la venta de entradas
            gestion_venta_entradas.venderEntradas()
        elif opcion == 3:
            # Se gestiona la asistencia a partidos
            gestion_asistencia_partidos.validarEntrada()
        elif opcion == 4:
            # Se gestionan los restaurantes
            gestion_restaurantes.gestionarRestaurante()
        elif opcion == 5:
            # Se gestiona la venta de productos de restaurantes
            gestion_venta_restauntes.venderProductos()
        elif opcion == 6:
            # Se muestran los indicadores de gestión (estadísticas)
            pass  # Implementar la funcionalidad para mostrar indicadores de gestión
        else:
            # Salir del bucle y terminar el programa
            break