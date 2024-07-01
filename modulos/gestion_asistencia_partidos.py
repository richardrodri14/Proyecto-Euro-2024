# Importar funciones necesarias desde utilidades
from utilidades.funciones import limpiarConsola, objetosDict
from utilidades.datos import guardarArchivo

# Definición de la clase GestionAsistenciaPartidos
class GestionAsistenciaPartidos:
    # Inicializador de la clase
    def __init__(self, entradas):
        self.entradas = entradas

    # Método para buscar una entrada por su código
    def buscarEntradaPorCodigo(self, codigo):
        for entrada in self.entradas:
            if codigo == entrada.codigo:
                return entrada
        return None

    # Método para preguntar si se desea repetir el proceso
    def repetir(self):
        eleccion = input("¿Desea ingresar un nuevo código? (Si/No): ")
        if eleccion.lower() == "si":
            self.validarEntrada()
            return
        elif eleccion.lower() == "no":
            return

    # Método para validar la entrada
    def validarEntrada(self):
        limpiarConsola()  # Limpiar la consola
        print("Bienvenido al módulo de Gestión de asistencia a partidos")
        codigo_str = input("Introduzca el código único de la entrada: ")
        entrada = self.buscarEntradaPorCodigo(codigo_str)
        if entrada == None:
            print("El código ingresado no es válido, por lo que la entrada no es auténtica")
            self.repetir()  # Preguntar si desea repetir
            return
        if entrada.usado:
            print("El código ingresado pertenece a una entrada que ya ha sido usada")
            self.repetir()  # Preguntar si desea repetir
            return
        entrada.usado = True  # Marcar la entrada como usada
        guardarArchivo("entradas", objetosDict(self.entradas))  # Guardar el estado actualizado de las entradas
        print("El código ingresado pertenece a una entrada válida y se ha registrado la asistencia")
        self.repetir()  # Preguntar si desea repetir