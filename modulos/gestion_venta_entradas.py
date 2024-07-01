from utilidades.partido import obtenerPartidoPorNumero, obtenerPartidoPorId
from utilidades.estadio import obtenerEstadioPorId
from utilidades.funciones import pedirDigito, pedirOpciones, preguntaSiNo, numeroLetras, esNumeroVampiro, tipoEntrada, limpiarConsola, objetosDict
from utilidades.datos import guardarArchivo
from modelos.entrada import Entrada
from modelos.cliente import Cliente

import math

class GestionVentaEntradas:
    def __init__(self, equipos, estadios, partidos, entradas, clientes):
        self.equipos = equipos
        self.estadios = estadios
        self.partidos = partidos
        self.entrada = None
        self.precio_general = 35
        self.precio_vip = 75
        self.asiento_general_icon = "."
        self.asiento_vip_icon = "*"
        self.asiento_ocupado_icon = "x"
        self.capacidad_filas = 10
        self.entradas = entradas
        self.clientes = clientes
        self.cliente = None
        self.registrado = False

    # Método para gestionar la venta de entradas
    def venderEntradas(self):
        limpiarConsola()
        print("Bienvenido al modulo de Gestión de venta de entradas")
        self.solicitarDatosCliente()  # Solicitar los datos del cliente
        if not self.cliente:
            return
        partido_id, tipo_entrada, asiento, precio = self.solicitarDatosVenta()  # Solicitar los datos de la venta

        limpiarConsola()

        descuento = 0
        if esNumeroVampiro(self.cliente.cedula):  # Verificar si la cédula es un número vampiro
            print("Felicidades su cedula es un numero vampiro, obtiene un %50 de descuento")
            descuento = precio * .5

        # Crear una nueva entrada con los datos obtenidos
        self.entrada = Entrada(self.cliente.id, partido_id, tipo_entrada, asiento, precio, descuento)
        self.mostrarInfo()  # Mostrar la información de la compra

        opcion = preguntaSiNo("¿Desea pagar la entrada? (Si/No): ")  # Preguntar si desea pagar la entrada
        
        if not opcion:
            opcion = preguntaSiNo("¿Desea volver a iniciar el proceso de compra? (Si/No): ")  # Preguntar si desea reiniciar la compra
            if opcion:
                self.venderEntradas()  # Reiniciar el proceso de venta de entradas
            return

        limpiarConsola()

        if not self.registrado:  # Registrar al cliente si no está registrado
            self.clientes.append(self.cliente)
            guardarArchivo("clientes", objetosDict(self.clientes))

        self.entradas.append(self.entrada)  # Añadir la entrada a la lista de entradas
        guardarArchivo("entradas", objetosDict(self.entradas))  # Guardar las entradas
        
        print("Su pago a sido exitoso, ¡Gracias por su compra!")

        opcion = preguntaSiNo("¿Desea realizar otra compra? (Si/No): ")  # Preguntar si desea realizar otra compra
        if opcion:
            self.venderEntradas()  # Reiniciar el proceso de venta de entradas

    # Método para mostrar la información de la compra
    def mostrarInfo(self):
        print("Resumen de la compra: ")
        print(f"-Nombre: {self.cliente.nombre}")
        print(f"-Cedula: {self.cliente.cedula}")
        print(f"-Edad: {self.cliente.edad}")
        print(f"-Codigo unico de entrada: {self.entrada.codigo}")
        print(f"-Tipo de entrada: {tipoEntrada(self.entrada.tipo)}")
        print(f"-Asiento: {self.entrada.asiento}")
        print(f"-Precio de la entrada: {self.entrada.precio}")
        print(f"-Descuento: {self.entrada.descuento}")
        print(f"-Subtotal: {self.entrada.obtenerSubtotal()}")
        print(f"-IVA: {self.entrada.obtenerIVA()}")
        print(f"-Total: {self.entrada.obtenerPrecioTotal()}")

    # Método para solicitar los datos del cliente
    def solicitarDatosCliente(self):
        limpiarConsola()

        cedula = pedirDigito("Ingrese la cédula del cliente: ", "La cedula del cliente no es valida, por favor introduzca una cedula valida")
        cliente = Cliente.obtenerClientePorCedula(self.clientes, cedula)

        if not cliente:  # Si el cliente no está registrado, solicitar más datos
            nombre = input("Ingrese el nombre del cliente: ").strip()
            edad = pedirDigito("Ingrese la edad del cliente: ", "La edad del cliente no es valida, por favor introduzca una edad valida")
            cliente = Cliente(nombre, cedula, edad)
        else:  # Si el cliente está registrado, preguntar si desea cargar su perfil
            print("Usted ya es un cliente registrado")
            opcion = preguntaSiNo("¿Desea cargar su perfil? (Si/No): ")
            if not opcion:
                self.venderEntradas()
                return
            self.registrado = True
        self.cliente = cliente

    # Método para mostrar las filas del estadio
    def mostrarFilas(self, estadio, filas_num, filas_totales, asientos_ocupados, tipo = "general"):
        tipo = tipo.lower()
        capacidad = estadio.capacidad[0]
        if tipo == "vip":
            capacidad = estadio.capacidad[1]

        espacios = math.ceil(filas_totales / 100)

        for i in range(0, filas_num):
            indice_fila = i + 1
            if tipo == "vip":
                indice_fila += math.ceil(estadio.capacidad[0]/ 10)
            resta_espacios = math.floor(indice_fila / 100)
            fila_num_asientos = 10
            fila_num_espacios = 0

            if i == filas_num - 1:
                fila_num_asientos = int(str(float(capacidad  / 10)).split(".")[1])
                fila_num_espacios = 10 - fila_num_asientos
            num_fila = str(indice_fila)
            if indice_fila < 10:
                num_fila += " "

            fila_asientos = f"{num_fila}" + " " * (espacios - resta_espacios) + "|"
            for j in range(1, fila_num_asientos + 1):
                asiento_icon = self.asiento_general_icon
                if tipo == "vip":
                    asiento_icon = self.asiento_vip_icon
                asiento = numeroLetras(j) + str(indice_fila)
                if asiento in asientos_ocupados:
                    asiento_icon = self.asiento_ocupado_icon
                fila_asientos += asiento_icon    
                if j < fila_num_asientos:
                    fila_asientos += " "
            fila_asientos += "  " * fila_num_espacios + "|"                   
            print(fila_asientos)

    # Método para obtener los asientos ocupados
    def obtenerAsientosOcupados(self, id_partido):
        asientos_ocupados = []
        for entrada in self.entradas:
            if id_partido == entrada.id_partido:
                asientos_ocupados.append(entrada.asiento)
        return asientos_ocupados

    # Método para obtener los asientos disponibles
    def obtenerAsientos(self, id_partido, tipo = "general"):
        tipo = tipo.lower()
        asientos = []
        partido = obtenerPartidoPorId(self.partidos, id_partido)
        estadio = obtenerEstadioPorId(self.estadios, partido.id_estadio)                
        filas_generales = math.ceil(estadio.capacidad[0] / 10)
        filas_vip = math.ceil(estadio.capacidad[1] / 10)
        filas_totales = filas_generales + filas_vip
        filas_num = filas_generales
        capacidad = estadio.capacidad[0]
        if tipo == "vip":
            capacidad = estadio.capacidad[1]

        if tipo == "vip":
            filas_num = filas_vip

        for i in range(0, filas_num):
            indice_fila = i + 1
            if tipo == "vip":
                indice_fila += math.ceil(estadio.capacidad[0]/ 10)
            fila_num_asientos = 10
            if i == filas_num - 1:
                fila_num_asientos = int(str(float(capacidad  / 10)).split(".")[1])
            for j in range(1, fila_num_asientos + 1):
                asiento = numeroLetras(j) + str(indice_fila)
                asientos.append(asiento)
        return asientos

    # Método para mostrar el mapa del estadio
    def mostrarMapaEstadio(self, id_partido):
        limpiarConsola()
        partido = obtenerPartidoPorId(self.partidos, id_partido)
        estadio = obtenerEstadioPorId(self.estadios, partido.id_estadio)

        print(f"Mapa del Estadio: {estadio.nombre}\n")
        print(f"Entradas Generales: \"{self.asiento_general_icon}\"")
        print(f"Entradas VIP: \"{self.asiento_vip_icon}\"")
        print(f"Entradas Ocupadas: \"{self.asiento_ocupado_icon}\"\n")

        asientos_ocupados = self.obtenerAsientosOcupados(id_partido)

        filas_generales = math.ceil(estadio.capacidad[0] / 10)
        filas_vip = math.ceil(estadio.capacidad[1] / 10)
        filas_totales = filas_generales + filas_vip
        espacios = math.ceil(filas_totales / 100)
        columnas_cabeceras = " " * espacios
        columnas_cabeceras += "   A B C D E F G H I J"
        columnas_separador = " " * espacios
        columnas_separador += "   -------------------"
        print(columnas_cabeceras)
        print(columnas_separador)

        self.mostrarFilas(estadio, filas_generales, filas_totales, asientos_ocupados)
        print(columnas_separador)
        self.mostrarFilas(estadio, filas_vip, filas_totales, asientos_ocupados, "vip")        

    # Método para verificar si un asiento es válido
    def esAsientoValido(self, asiento, id_partido, tipo_entrada = "general"):
        asientos = self.obtenerAsientos(id_partido, tipo_entrada)
        return asiento in asientos

    # Método para verificar si un asiento está ocupado
    def esAsientoOcupado(self, asiento, id_partido):
        asientos_ocupados = self.obtenerAsientosOcupados(id_partido)
        return asiento in asientos_ocupados
    
    # Método para seleccionar un asiento
    def seleccionarAsiento(self, id_partido, tipo_entrada):
        asiento = input("\nSeleccione el asiento: ").upper().strip()
        asiento_valido = self.esAsientoValido(asiento, id_partido, tipoEntrada(tipo_entrada))
        asiento_ocupado = self.esAsientoOcupado(asiento, id_partido)
        while not asiento_valido or asiento_ocupado:
            if not asiento_valido:
                print("El asiento seleccionado no corresponde al tipo de entrada, por favor selecciona un asiento valido")
            if asiento_ocupado:
                print("El asiento seleccionado ya esta ocupado, por favor selecciona un asiento valido")
            asiento = input("\nSeleccione el asiento: ").upper().strip()
            asiento_valido = self.esAsientoValido(asiento, id_partido, tipoEntrada(tipo_entrada))
            asiento_ocupado = self.esAsientoOcupado(asiento, id_partido)
        return asiento
    
    # Método para mostrar los partidos disponibles
    def mostrarPartidos(self):
        print("Partidos disponibles:")

        for partido in self.partidos:
            nombre_equipo_local = partido.obtenerEquipo(self.equipos).nombre
            nombre_equipo_visitante = partido.obtenerEquipo(self.equipos, False).nombre
            nombre_estadio = partido.obtenerEstadio(self.estadios).nombre
            print(f"\nPartido Numero: {partido.numero}")
            print(f"Equipo Local: {nombre_equipo_local}")
            print(f"Equipo Visitante: {nombre_equipo_visitante}")
            print(f"Grupo: {partido.grupo}")
            print(f"Fecha: {partido.fecha_hora}")
            print(f"Estadio: {nombre_estadio}")

    # Método para solicitar los datos de la venta
    def solicitarDatosVenta(self):

        limpiarConsola()
        self.mostrarPartidos()  # Mostrar los partidos disponibles

        numero_partido = pedirDigito("\nIngrese el numero del partido: ", "Debe ingresar un numero de partido valido")
        
        partido = obtenerPartidoPorNumero(self.partidos, numero_partido)
        while partido == None:
            print("El numero del partido no es valido, por favor ingrese un numero valido")
            numero_partido = pedirDigito("\nIngrese el numero del partido: ", "Debe ingresar un numero de partido valido")
            partido = obtenerPartidoPorNumero(self.partidos, numero_partido)

        limpiarConsola()

        tipo_entrada = pedirOpciones("Tipos de entradas:", "\nSeleccione el tipo de entrada, ingresando el numero correspondiente a la opcion: ", [
            "1. General ($35)",
            "2. Vip ($75)"
        ], "La opcion seleccionada no es valida, por favor introduzca una opcion valida")
        
        precio = self.precio_general
        
        if tipo_entrada == 2:
            precio = self.precio_vip
        
        self.mostrarMapaEstadio(partido.id)  # Mostrar el mapa del estadio

        asiento = self.seleccionarAsiento(partido.id, tipo_entrada)  # Seleccionar el asiento
        
        return partido.id, tipo_entrada, asiento, precio  # Retornar los datos de la venta