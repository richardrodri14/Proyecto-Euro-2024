from itertools import permutations
from datetime import datetime
import os

# Función para mostrar todos los elementos de un arreglo
def mostrarTodo(arreglo):
  print("\n")
  for elemento in arreglo:
    elemento.mostrar()

# Función para convertir un número en su correspondiente representación de letras
# (ej. 1 -> 'A', 27 -> 'AA')
def numeroLetras(n):
  resultado = ""
  while n > 0:
      n -= 1
      resultado = chr(n % 26 + 65) + resultado
      n //= 26
  return resultado

# Función para determinar si un número es un número vampiro
def esNumeroVampiro(num):
    # Convertir el número a cadena
    num = int(num)
    num_str = str(num)
    
    # Comprobar si la longitud es par
    if len(num_str) % 2 != 0:
        return False

    # Calcular la mitad de la longitud
    mitad = len(num_str) // 2
    
    # Generar todas las permutaciones posibles de los dígitos
    permutaciones = set(permutations(num_str))

    # Recorrer cada permutación
    for perm in permutaciones:
        # Dividir la permutación en dos factores
        f1 = int(''.join(perm[:mitad]))
        f2 = int(''.join(perm[mitad:]))
        
        # Comprobar si el producto de los factores es igual al número original
        # y que no terminen ambos en 0
        if f1 * f2 == num and not (str(f1).endswith('0') and str(f2).endswith('0')):
            return True

    # Si ninguna permutación cumple la condición, no es un número vampiro
    return False

# Función para clasificar un número en una categoría de producto específica
def numeroClasificacion(num):
  num = int(num)
  if num == 1:
    return "alcoholic"
  elif num == 2:
    return "non-alcoholic"
  elif num == 3:
    return "package"
  elif num == 4:
    return "plate"
  return ""

# Función para determinar el tipo de entrada basado en un número
def tipoEntrada(num):
  if int(num) == 1:
    return "General"
  else:
    return "VIP"

# Función para convertir el tipo de entrada en su representación de cadena
def convertirEntradaStr(num):
  if int(num) == 1:
    return "General"
  else:
    return "VIP"

# Función para convertir el tipo de entrada en su representación numérica
def convertirEntradaInt(entrada):
  if str(entrada).lower() == "general":
    return 1
  else:
    return 2

# Función para limpiar la consola
def limpiarConsola():
  # Limpiar la consola (comando para Windows y Unix)
  os.system('cls' if os.name == 'nt' else 'clear')

# Función para convertir un objeto en un diccionario
def objetoDict(obj):
    if isinstance(obj, dict):
        return {k: objetoDict(v) for k, v in obj.items()}
    elif hasattr(obj, "__dict__"):
        return {k: objetoDict(v) for k, v in obj.__dict__.items()}
    elif isinstance(obj, list):
        return [objetoDict(item) for item in obj]
    else:
        return obj

# Función para convertir una lista de objetos en una lista de diccionarios
def objetosDict(objetos):
  nuevos_objetos = []
  for objeto in objetos:
    nuevos_objetos.append(objetoDict(objeto))
  return nuevos_objetos

# Función para convertir una clasificación en su correspondiente descripción
def convertirClasificacion(clasificacion):
  if clasificacion == "alcoholic":
    return "Bebidas (Alcohólicas)"
  if clasificacion == "non-alcoholic":
    return "Bebidas (No Alcohólicas)"
  if clasificacion == "package":
    return "Alimento (Empaquetado)"
  if clasificacion == "plate":
    return "Alimento (De preparación)"

# Función para hacer una pregunta de sí/no al usuario
def preguntaSiNo(mensaje, error = ""):
  opcion = input(mensaje).lower().strip()
  if error == "":
    error = "La opción seleccionada no es válida, por favor introduzca una opción válida (Sí/No)"
  while opcion != "si" and opcion != "no":
    print(error)
    opcion = input(mensaje).lower().strip()
  if opcion == "si":
    return True
  return False

# Función para pedir un dígito al usuario
def pedirDigito(mensaje, error = ""):
  digito = input(mensaje).strip()
  if error == "":
    error = "Por favor introduzca un dígito válido"
  while not str.isdigit(digito) or int(digito) < 1:
    print(error)
    digito = input(mensaje).strip()
  return int(digito)

# Función para pedir una opción al usuario de una lista de opciones
def pedirOpciones(inicial, mensaje, opciones, error = ""):
  print(inicial)
  for opcion in opciones:
    print(opcion)
  n = len(opciones)
  digito = pedirDigito(mensaje, error)
  while digito < 1 or digito > n:
    digito = pedirDigito(mensaje, error)
  return digito

# Función para pedir una fecha al usuario
def pedirFecha(mensaje, error = ""):
  fecha_str = input(mensaje).strip()
  while True:
    try:
      fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
      return fecha
    except ValueError:
      print(error)
      fecha_str = input(mensaje).strip()

# Función para determinar si un número es perfecto
def esNumeroPerfecto(num):
  num = int(num)
  suma = 0
  for i in range(1, num):
    if (num % i == 0):
      suma += i
 
  if num == suma:
    return True
  else:
    return False

