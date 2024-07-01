from modelos.cliente import Cliente
from modelos.entrada import Entrada
from modelos.restaurante import Restaurante
from modelos.partido import Partido
from modelos.compra import Compra
from utilidades.funciones import preguntaSiNo, pedirDigito, pedirOpciones, esNumeroPerfecto, limpiarConsola, objetosDict
from utilidades.datos import guardarArchivo
from utilidades.funciones import convertirClasificacion

class GestionVentaRestaurantes:
    def __init__(self, estadios, restaurantes, partidos, clientes, compras, entradas):
        self.estadios = estadios  # Lista de estadios
        self.restaurantes = restaurantes  # Lista de restaurantes
        self.partidos = partidos  # Lista de partidos
        self.compras = compras  # Lista de compras
        self.entradas = entradas  # Lista de entradas
        self.clientes = clientes  # Lista de clientes
        self.reiniciar()  # Inicializa los atributos del cliente

    def reiniciar(self):
        self.restaurantes_cliente = []  # Restaurantes asociados al cliente
        self.cliente = None  # Cliente actual
        self.pedidos = []  # Pedidos del cliente
        self.entradas_cliente = []  # Entradas del cliente

    def solicitarDatosCliente(self):
        cedula = pedirDigito("Ingrese la cédula del cliente: ", "La cedula del cliente no es valida, por favor introduzca una cedula valida")  # Solicita la cédula del cliente
        cliente = Cliente.obtenerClientePorCedula(self.clientes, cedula)  # Busca al cliente por cédula
        if not cliente:
            print("Su cedula no coincide con la de ningun cliente")  # Mensaje si no se encuentra al cliente
            opcion = preguntaSiNo("¿Desea intentarlo nuevamente? (Si/No): ")
            if opcion:
                self.solicitarDatosCliente()  # Vuelve a solicitar los datos del cliente
            return
        entradas_cliente = Entrada.obtenerEntradasPorIdCliente(self.entradas, cliente.id)  # Obtiene las entradas del cliente
        if len(entradas_cliente) == 0:
            print("Usted no posee ninguna entrada")  # Mensaje si no tiene entradas
            opcion = preguntaSiNo("¿Desea intentar nuevamente el proceso comprar? (Si/No): ")
            if opcion:
                self.venderProductos()  # Vuelve al proceso de venta de productos
            return
        entradas_cliente = Entrada.obtenerEntradasPorTipo(entradas_cliente, "vip")  # Filtra entradas VIP
        if len(entradas_cliente) == 0:
            print("Usted no posee ninguna entrada de tipo VIP")  # Mensaje si no tiene entradas VIP
            opcion = preguntaSiNo("¿Desea intentar nuevamente el proceso comprar? (Si/No): ")
            if opcion:
                self.venderProductos()  # Vuelve al proceso de venta de productos
            return
        limpiarConsola()
        print("Felicidades usted es un cliente VIP")  # Mensaje si es cliente VIP
        self.entradas_cliente = entradas_cliente
        self.cliente = cliente        
                    
    def solicitarDatosVenta(self):
        ids_partidos = [entrada.id_partido for entrada in self.entradas]  # IDs de partidos a partir de las entradas
        partidos = Partido.obtenerPartidosPorIDs(self.partidos, ids_partidos)  # Obtiene partidos por IDs
        estadios_cliente = []
        for partido in partidos:
            estadio = partido.obtenerEstadio(self.estadios)  # Obtiene el estadio del partido
            if not estadio in estadios_cliente:
                estadios_cliente.append(estadio)  # Añade el estadio a la lista si no está ya incluido
        for estadio in estadios_cliente:
            self.restaurantes_cliente += estadio.restaurantes  # Añade los restaurantes del estadio a la lista de restaurantes del cliente

        opcion = pedirOpciones("¿Desea elegir un restaurante o ver los productos de todos los restaurantes a los que tiene acceso?", "\nSeleccione la opcion ingresando su numero correspondiente: ", [
                "1. Elegir un restaurante",
                "2. Todos"
            ], 
            "La opcion seleccionada no es valida, por favor introduzca una opcion valida"
        )

        limpiarConsola()
        if opcion == 1:
            lista_restaurantes = Restaurante.obtenerListaRestaurantes(self.restaurantes_cliente)  # Obtiene la lista de restaurantes
            opcion = pedirOpciones("Restaurantes:", "\nSeleccione el restaurante, ingresando el numero correspondiente a la opcion: ", 
                lista_restaurantes, 
                "La opcion seleccionada no es valida, por favor introduzca una opcion valida"
            )
            restaurante_seleccionado = self.restaurantes_cliente[opcion - 1]  # Selecciona el restaurante
            self.restaurantes_cliente = []
            self.restaurantes_cliente.append(restaurante_seleccionado)   
        
        productos = []
        for restaurante in self.restaurantes_cliente:
            productos += restaurante.productos  # Añade los productos del restaurante a la lista de productos
        for i, producto in enumerate(productos):
            producto.mostrar(i + 1, False)  # Muestra los productos

        while True:
            numero_producto = pedirDigito("\nIngrese el numero del producto: ", "Debe ingresar un numero de producto valido")  # Solicita el número del producto
            while numero_producto > len(productos):
                print("El numero del producto no es valido, por favor ingrese un numero valido")  # Mensaje si el número del producto no es válido
                numero_producto = pedirDigito("\nIngrese el numero del producto: ", "Debe ingresar un numero de producto valido")

            unidades = pedirDigito("Ingrese el numero de unidades que sea: ", "Debe ingresar un numero de unidades valido")  # Solicita el número de unidades
            
            producto = productos[numero_producto - 1]
            pedido = {
                "nombre" : producto.nombre,
                "precio" : producto.precio,
                "clasificacion" : producto.clasificacion,
                "cantidad" : unidades
            }
            if self.cliente.edad < 18 and producto.clasificacion == "alcoholic":
                print("Usted es menor de 18 años, no puede comprar productos alcolicos")  # Mensaje si el cliente es menor de 18 y el producto es alcohólico
            else:
                self.pedidos.append(pedido)  # Añade el pedido a la lista de pedidos
            opcion = preguntaSiNo("¿Desea agregar otro producto? (Si/No): ")
            if not opcion:
                break
            
    def venderProductos(self):
        limpiarConsola()
        print("Bienvenido al modulo de Gestión de venta de restaurantes")
        self.reiniciar()  # Reinicia los atributos del cliente
        self.solicitarDatosCliente()  # Solicita los datos del cliente
        if not self.cliente:
            return
        self.solicitarDatosVenta()  # Solicita los datos de la venta

        limpiarConsola()
        if len(self.pedidos) == 0:
            return 
        
        descuento = 0
        if esNumeroPerfecto(self.cliente.cedula):
            print("Felicidades su cedula es un numero perfecto, obtiene un %15 de descuento")  # Mensaje si la cédula es un número perfecto
            descuento = precio * .15
        self.compra = Compra(self.cliente.id, self.pedidos, descuento)  # Crea una nueva compra
        self.mostrarInfo()  # Muestra la información de la compra

        opcion = preguntaSiNo("¿Desea pagar los productos? (Si/No): ")
        if not opcion:
            opcion = preguntaSiNo("¿Desea volver a iniciar el proceso de compra? (Si/No): ")
            if opcion:
                self.venderProductos()  # Vuelve al proceso de venta de productos
            return

        limpiarConsola()

        self.compras.append(self.compra)  # Añade la compra a la lista de compras
        guardarArchivo("compras", objetosDict(self.compras))  # Guarda la lista de compras en un archivo
        Restaurante.actualizarProductosRestaurantes(self.restaurantes, self.compras)  # Actualiza los productos de los restaurantes
        print("Su pago a sido exitoso, ¡Gracias por su compra!")

        opcion = preguntaSiNo("¿Desea realizar otra compra? (Si/No): ")
        if opcion:
            self.venderProductos()  # Vuelve al proceso de venta de productos

    def mostrarInfo(self):
        print("Datos del cliente: ")
        print(f" -Nombre: {self.cliente.nombre}")
        print(f" -Cedula: {self.cliente.cedula}")
        print(f" -Edad: {self.cliente.edad}")
        print("\nProductos: ")
        for pedido in self.pedidos:
            print(f" -Nombre: {pedido['nombre']}")
            print(f" -Precio: {pedido['precio']}")
            print(f" -Clasificacion: {convertirClasificacion(pedido['clasificacion'])}")
            print(f" -Cantidad: {pedido['cantidad']}\n")
        print("Resumen de la compra: ")
        print(f" -Descuento: {self.compra.descuento}")
        print(f" -Subtotal: {self.compra.obtenerSubtotal()}")
        print(f" -IVA: {self.compra.obtenerIVA()}")
        print(f" -Total: {self.compra.obtenerPrecioTotal()}")



