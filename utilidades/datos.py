from modelos.equipo import Equipo
from modelos.estadio import Estadio
from modelos.partido import Partido
from modelos.producto import Producto
from modelos.restaurante import Restaurante
from modelos.cliente import Cliente
from modelos.compra import Compra
from modelos.entrada import Entrada

from datetime import datetime
import requests
import json

def cargarDatosArchivos():
    # Cargar datos de clientes, compras y entradas desde archivos
    clientes = cargarClientes()
    compras = cargarCompras()
    entradas = cargarEntradas()
    return clientes, compras, entradas

def cargarArchivo(archivo):
    # Abrimos el archivo TXT en modo lectura
    ruta = f"archivos/{archivo}.txt"
    with open(ruta, 'r') as archivo_txt:
        # Cargamos el contenido del archivo en un objeto Python
        try:
            datos = json.load(archivo_txt)
        except Exception as e:
            datos = []
    return datos

def cargarClientes():
    # Cargar datos de clientes desde archivo
    clientes_data = cargarArchivo("clientes")
    clientes = []
    for cliente in clientes_data:
        id = cliente['id']
        nombre = cliente['nombre']
        cedula = cliente['cedula']
        edad = cliente['edad']
        # Crear una instancia de Cliente y agregarla a la lista
        nuevo_cliente = Cliente(nombre, cedula, edad, id)
        clientes.append(nuevo_cliente)
    return clientes

def cargarCompras():
    # Cargar datos de compras desde archivo
    compras_data = cargarArchivo("compras")
    compras = []
    for compra in compras_data:
        id = compra['id']
        pedidos = compra['pedidos']
        descuento = compra['descuento']
        id_cliente = compra['id_cliente']
        # Crear una instancia de Compra y agregarla a la lista
        nuevo_compra = Compra(id_cliente, pedidos, descuento, id)
        compras.append(nuevo_compra)
    return compras

def cargarEntradas():
    # Cargar datos de entradas desde archivo
    entradas_data = cargarArchivo("entradas")
    entradas = []
    for entrada in entradas_data:
        codigo = entrada['codigo']
        descuento = entrada['descuento']
        precio = entrada['precio']
        asiento = entrada['asiento']
        tipo = entrada['tipo']
        id_partido = entrada['id_partido']
        id_cliente = entrada['id_cliente']
        # Crear una instancia de Entrada y agregarla a la lista
        nuevo_entrada = Entrada(id_cliente, id_partido, tipo, asiento, precio, descuento, codigo)
        entradas.append(nuevo_entrada)
    return entradas

def guardarArchivo(archivo, datos):
    # Guardar datos en un archivo TXT
    with open(f"archivos/{archivo}.txt", 'w') as archivo:
        json.dump(datos, archivo, indent=4)

def cargarDatosAPI():
    # Cargar datos de equipos, estadios y partidos desde una API
    equipos = cargarEquipos()
    estadios = cargarEstadios()
    partidos = cargarPartidos()
    return equipos, estadios, partidos

def cargarEquipos():
    # Cargar datos de equipos desde la API
    equipos = []
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json"
    response = requests.get(url)
    equipos_data = response.json()
    for equipo in equipos_data:
        id = equipo['id']
        nombre = equipo['name']
        codigo_fifa = equipo['code']
        grupo = equipo['group']
        # Crear una instancia de Equipo y agregarla a la lista
        nuevo_equipo = Equipo(id, nombre, codigo_fifa, grupo)
        equipos.append(nuevo_equipo)
    return equipos

def cargarEstadios():
    # Cargar datos de estadios desde la API
    estadios = []
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json"
    response = requests.get(url)
    estadios_data = response.json()
    for estadio in estadios_data:
        id = estadio['id']
        nombre = estadio['name']
        ciudad = estadio['city']
        capacidad = estadio['capacity']
        restaurantes = []
        restaurantes_data = estadio['restaurants']
        for restaurante in restaurantes_data:
            productos = []
            restaurante_nombre = restaurante['name']
            productos_data = restaurante['products']
            for producto in productos_data:
                producto_nombre = producto['name']
                cantidad = producto['quantity']
                clasificacion = producto['adicional']
                precio = float(producto['price'])
                precio += precio * .16
                unidades = producto['stock']
                # Crear una instancia de Producto y agregarla a la lista de productos
                nuevo_producto = Producto(producto_nombre, cantidad, clasificacion, precio, unidades)
                productos.append(nuevo_producto)
            # Crear una instancia de Restaurante y agregarla a la lista de restaurantes
            nuevo_restaurante = Restaurante(restaurante_nombre, productos)
            restaurantes.append(nuevo_restaurante)
        # Crear una instancia de Estadio y agregarla a la lista
        nuevo_estadio = Estadio(id, nombre, ciudad, capacidad, restaurantes)
        estadios.append(nuevo_estadio)
    return estadios

def cargarPartidos():
    # Cargar datos de partidos desde la API
    partidos = []
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json"
    response = requests.get(url)
    partidos_data = response.json()
    for partido in partidos_data:
        id = partido['id']
        numero = partido['number']
        id_equipo_local = partido['home']['id']
        id_equipo_visitante = partido['away']['id']
        id_estadio = partido['stadium_id']
        fecha_hora = partido['date']
        grupo = partido['group']
        # Crear una instancia de Partido y agregarla a la lista
        nuevo_partido = Partido(id, numero, id_equipo_local, id_equipo_visitante, fecha_hora, grupo, id_estadio)
        partidos.append(nuevo_partido)
    return partidos