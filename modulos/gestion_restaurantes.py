# Importar la función limpiarConsola desde el módulo utilidades.funciones
from utilidades.funciones import limpiarConsola

# Definición de la clase GestionRestaurantes
class GestionRestaurantes:
    # Inicializador de la clase
    def __init__(self, estadios):
        self.estadios = estadios

    # Método para mostrar una lista de productos
    def mostrarProductos(self, productos):
        if len(productos) == 0:
            print("No se encontraron productos")
        for producto in productos:
            if producto:
                producto.mostrar()

    # Método para gestionar la búsqueda y visualización de restaurantes y sus productos
    def gestionarRestaurante(self):
        limpiarConsola()  # Limpiar la consola
        print("Bienvenido al módulo de Gestión de restaurantes")
        print("¿Desea elegir un restaurante o buscar en todos?")
        print("1. Elegir un restaurante")
        print("2. Todos")

        # Pedir al usuario que elija una opción
        opcion = input("\nIngrese el número correspondiente a la opción: ").strip()
        while opcion != "1" and opcion != "2":
            print("La opción seleccionada no es válida, por favor introduzca una opción válida")
            opcion  = input("\nIngrese el número correspondiente a la opción: ").strip()
       
        limpiarConsola()  # Limpiar la consola
        restaurantes = []
        for estadio in self.estadios:
            for restaurante in estadio.restaurantes:
                restaurantes.append(restaurante)

        # Si el usuario elige buscar en un restaurante específico
        if opcion == "1":
            print("Restaurantes: ")
            i = 1
            for restaurante in restaurantes:
                print(f"{i}. {restaurante.nombre}")
                i += 1
            opcion = input("\nSeleccione un restaurante introduciendo el número correspondiente: ").strip()
            while not str.isdigit(opcion) or int(opcion) < 1 or int(opcion) > len(restaurantes):
                print("La opción seleccionada no es válida, por favor introduzca una opción válida")
                opcion = input("\nSeleccione un restaurante introduciendo el número correspondiente: ").strip()
            restaurantes = [restaurantes[int(opcion) - 1]]
        
        limpiarConsola()  # Limpiar la consola
        print("¿Por cuál criterio desea buscar los productos?")
        print("1. Por nombre")
        print("2. Por tipo")
        print("3. Por rango de precio")

        # Pedir al usuario que elija un criterio de búsqueda
        opcion = input("\nIngrese el número correspondiente a la opción: ").strip()
        while opcion != "1" and opcion != "2" and opcion != "3":
            print("La opción seleccionada no es válida, por favor introduzca una opción válida")
            opcion  = input("\nIngrese el número correspondiente a la opción: ").strip()

        limpiarConsola()  # Limpiar la consola
        if opcion == "1":
            # Buscar productos por nombre
            nombre = input("\nIngrese el nombre del producto: ").strip()
            productos = []
            for restaurante in restaurantes:
                productos_encontrados = restaurante.buscarProductoPorNombre(nombre)
                productos += productos_encontrados
            self.mostrarProductos(productos)
        elif opcion == "2":
            # Buscar productos por tipo
            print("¿Qué tipo de productos desea buscar?")
            print("1. Bebidas (Alcohólicas)")
            print("2. Bebidas (No Alcohólicas)")
            print("3. Alimento (Empaquetado)")
            print("4. Alimento (De preparación)")
            opcion = input("\nIngrese el número correspondiente a la opción: ").strip()
            while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4":
                print("La opción seleccionada no es válida, por favor introduzca una opción válida")
                opcion  = input("\nIngrese el número correspondiente a la opción: ").strip()
            productos = []
            for restaurante in restaurantes:
                productos_encontrados = restaurante.buscarProductoPorClasificacion(opcion)
                productos += productos_encontrados
            self.mostrarProductos(productos)
        else:
            # Buscar productos por rango de precio
            minimo = input("Ingrese el precio mínimo: ")
            maximo = input("Ingrese el precio máximo: ")
            productos = []
            for restaurante in restaurantes:
                productos_encontrados = restaurante.buscarProductoPorPrecio(minimo, maximo)
                productos += productos_encontrados
            self.mostrarProductos(productos)
        
        # Preguntar si desea buscar más productos
        eleccion = input("¿Desea buscar más productos? (Sí/No): ")
        if eleccion.lower() == "si":
            self.gestionarRestaurante()
            return
        elif eleccion.lower() == "no":
            return